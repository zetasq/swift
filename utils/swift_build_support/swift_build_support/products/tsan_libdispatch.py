# swift_build_support/products/tsan_libdispatch.py --------------*- python -*-
#
# This source file is part of the Swift.org open source project
#
# Copyright (c) 2014 - 2019 Apple Inc. and the Swift project authors
# Licensed under Apache License v2.0 with Runtime Library Exception
#
# See https://swift.org/LICENSE.txt for license information
# See https://swift.org/CONTRIBUTORS.txt for the list of Swift project authors
#
# ----------------------------------------------------------------------------

import os

from . import product
from .. import shell


class TSanLibDispatch(product.Product):
    @classmethod
    def product_source_name(cls):
        return "tsan-libdispatch-test"

    @classmethod
    def is_build_script_impl_product(cls):
        return False

    def build(self, host_target):
        """We reuse the llvm build directory."""
        # Clang is already built. TSan runtime will be built by 'check-tsan' in
        # test step.
        pass

    def test(self, host_target):
        """Run check-tsan target with a LIT filter for libdispatch."""
        llvm_build_dir = os.path.join(self.build_dir, '..', 'llvm-'+host_target)
        cmd = ['cmake', '--build', llvm_build_dir, '--target', 'check-tsan']
        env = {'LIT_FILTER': 'libdispatch'}
        shell.call(cmd, env=env)
