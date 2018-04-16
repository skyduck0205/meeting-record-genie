/**
 * Creates a menu entry in the Google Docs UI when the document is opened.
 *
 * @param {object} e The event parameter for a simple onOpen trigger. To
 *     determine which authorization mode (ScriptApp.AuthMode) the trigger is
 *     running in, inspect e.authMode.
 */
function onOpen(e) {
  DocumentApp.getUi()
    .createAddonMenu()
    .addItem('Start', 'showSidebar')
    .addToUi();

  var prefs = getPreferences();
  if (prefs.autoOpen === 'true') {
    showSidebar();
  }
}

/**
 * Runs when the add-on is installed.
 *
 * @param {object} e The event parameter for a simple onInstall trigger. To
 *     determine which authorization mode (ScriptApp.AuthMode) the trigger is
 *     running in, inspect e.authMode. (In practice, onInstall triggers always
 *     run in AuthMode.FULL, but onOpen triggers may be AuthMode.LIMITED or
 *     AuthMode.NONE.)
 */
function onInstall(e) {
  onOpen(e);
}

/**
 * Opens a sidebar in the document containing the add-on's user interface.
 */
function showSidebar() {
  var ui = HtmlService.createHtmlOutputFromFile('Sidebar')
    .setTitle('Meeting Record Genie')
    .setSandboxMode(HtmlService.SandboxMode.IFRAME);
  DocumentApp.getUi().showSidebar(ui);
}

////////

// Set add-on preferences
function setPreferences(props) {
  var userProperties = PropertiesService.getUserProperties();
  for (var key in props) {
    userProperties.setProperty(key, props[key]);
  }
}

// Get add-on preferences
function getPreferences() {
  var userProperties = PropertiesService.getUserProperties();
  return {
    recorder: userProperties.getProperty('recorder'),
    autoOpen: userProperties.getProperty('autoOpen')
  };
}

// Submit queries and get record data
function submitRecord(input) {
  setPreferences({
    recorder: input.recorder
  });

  var text = DocumentApp.getActiveDocument()
    .getBody()
    .getText();
  var lines = text.split('\n');

  input.lines = _filterRecordsByDate(input.date, lines);
  input.data = _handleLines(input);
  input.rstText = _buildRst(input);

  return input;
}

// Dump unused texts
function _filterRecordsByDate(date, lines) {
  var filtered = [],
    dateFound = false;

  for (var i = 0; i < lines.length; i++) {
    var line = _trimLine(lines[i]);
    if (/^\d+\/\d+\/\d+$/.test(line)) {  // Find string with format YYYY/MM/DD
      // Break loop if date is found before and get another date
      if (dateFound) { break; }
      // Replace - to / to prevent time difference between utc/locale
      dateFound = new Date(date.replace(/-/g, '/')) - new Date(line) === 0;
      // Do not push date string into lines
      if (dateFound) { continue; }
    }

    if (dateFound && !/^\s*$/.test(line)) { // not empty string
      filtered.push(line);
    }
  }

  return filtered;
}

// Get dones and todos of members
function _handleLines(input) {
  var data = [],
    currentData,
    state = 'done';

  input.lines.forEach(function(line) {
    var user = _findInList(input.userList, line);
    if (user) {
      currentData = {
        user: user,
        done: [],
        todo: []
      };
      data.push(currentData);
    } else if (line === '進度') {
      state = 'done';
    } else if (line === '預計') {
      state = 'todo';
    } else {
      currentData[state].push(line + '。');
    }
  });
  return data;
}

function _buildRst(input) {
  // Handle head
  var attendants = input.data.map(function(x){
    return x.user.tw + '(' + x.user.en + ')';
  });
  var row = Math.ceil((attendants.length + 1) / 5);
  var rst = [
    ':DocNumber:      Company(M)' + input.date.replace(/-/g, '') + '-01',
    '\n:Subject:        例行早會',
    '\n:Date:           ' + input.date.replace(/-/g, '.') + '(' + input.day + ')',
    '\n:Time:           ' + input.startTime + ' - ' + input.endTime,
    '\n:LocationMain:   ' + input.loc0,
    '\n:LocationSub:    ' + input.loc1,
    '\n:Recorder:       ' + input.recorder,
    '\n:Meeting_Row:    ' + row,
    '\n:Meeting_Participants:     ' + attendants.join('、') + '\\ \\ \\ ',
    '\n\n.. HEADER',
    '\n\n機密等級：□ 極機密　■ 密件  □ 一般件  □ 其他',
    '\n\n重點摘要：',
    '\n\n.. raw:: latex',
    '\n\n   \\vspace{0.4cm}',
    '\n\n一.各成員任務進度及目標報告：'
  ];

  // Handle body
  var i, j;
  for (i = 0; i < input.data.length; i++) {
    var data = input.data[i];

    if (data.done.length || data.todo.length) {
      rst.push('\n\n   #) ' + data.user.en + '：\n');
      // done
      for (j = 0; j < data.done.length; j++) {
        var num = j === 0 ? 'a' : '#';
        rst.push('\n      ' + num + ') 進度：' + data.done[j]);
      }
      for (j = 0; j < data.todo.length; j++) {
        rst.push('\n      #) 預計：' + data.todo[j]);
      }
    }
  }

  rst.push('\n\n以上。');

  return rst.join('');
}

// Remove trailing punctuations of a string
function _trimLine(string) {
  return string.trim()
    .replace(/ *(:|：)$/, '')
    .replace(/ *(\.|。)$/, '');
}

// Check if string is a name
function _findInList(list, string, key) {
  var index = list.map(function(item) { return item[key || 'en']; }).indexOf(string);
  return index >= 0 ? list[index] : null;
}
