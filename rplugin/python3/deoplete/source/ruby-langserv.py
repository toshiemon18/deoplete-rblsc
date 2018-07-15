import pathlib
import json
import re
import subprocess

from deoplete.util import getlines, expand
from .base import Base
from solargraph.client import Client


class Source(Base):
    def __init__(self, vim):
        self.name = "ruby-langserv"
        self.filetypes = ['ruby']
        self.mark = '[rb-langserv]'
        self.rank = 900
        self.input_pattern = r'\.[a-zA-Z0-9_?!]+|[a-zA-Z]\w*::\w*'
        self.langserv_status = False
        super(Source, self).__init__(vim)

    def get_complete_position(self, context):
        pass

    def gather_candidates(self, context):
        pass
