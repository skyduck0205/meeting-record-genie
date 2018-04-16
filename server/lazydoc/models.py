# -*- coding: utf-8 -*-
import os
from django.conf import settings

class LazyDoc(object):
    RST_PATH = settings.RST_PATH
    RST_BUILD_PATH = settings.RST_BUILD_PATH
    PDF_PATH = settings.PDF_PATH

    def __init__(self):
        pass

    def create_rst(self, raw, filename):
        """create rst file"""
        if not os.path.isdir(self.RST_PATH):
            os.makedirs(self.RST_PATH)

        file_path = os.path.join(self.RST_PATH, filename)
        f = open(file_path, 'w')
        f.write(raw)
        f.close()
        cmd = 'chmod 666 {}'.format(file_path)
        os.system(cmd)
        return file_path

    def create_pdf(self, rst_filename, pdf_filename):
        """create pdf file"""
        if not os.path.isdir(self.PDF_PATH):
            os.makedirs(self.PDF_PATH)

        pdf_file = os.path.join(self.RST_PATH, pdf_filename)

        # A script command to build pdf from rst
        cmd = (
            'cd {rst_build};'
            './target.sh {rst_file};'
            'timeout 15s make -k > /dev/null;'
            'make clean;'
        ).format(
            rst_build=self.RST_BUILD_PATH,
            rst_file=rst_filename
        )
        # os.system(cmd)

        if not os.path.isfile(pdf_file):
            print 'Build pdf file failed'
            return 'None'
        else:
            print 'Build pdf file done'

        # move to pdf path
        cmd = (
            'chmod 666 {pdf_file};'
            'mv {pdf_file} {pdf_path};'
        ).format(
            pdf_file=pdf_file,
            pdf_path=self.PDF_PATH
        )
        # os.system(cmd)
        return os.path.join(self.PDF_PATH, pdf_filename)
