# Copyright 2017, Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
import os
import pathlib

import nox


CURRENT_DIRECTORY = pathlib.Path(__file__).parent.absolute()


PYTHON_VERSIONS = [
    "3.6",
    "3.7",
    "3.8",
    "3.9",
    "3.10",
    "3.11",
    "3.12",
]

# Error if a python version is missing
nox.options.error_on_missing_interpreters = True


@nox.session(python=PYTHON_VERSIONS)
def unit(session, proto="python"):
    """Run the unit test suite."""

    constraints_path = str(
        CURRENT_DIRECTORY / "testing" / f"constraints-{session.python}.txt"
    )

    session.env["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = proto
    session.install("coverage", "pytest", "pytest-cov", "pytz")
    session.install("-e", ".[testing]", "-c", constraints_path)
    if proto == "cpp":  # 4.20 does not have cpp.
        session.install("protobuf==3.19.0")

    # TODO(https://github.com/googleapis/proto-plus-python/issues/403): re-enable `-W=error`
    # The warnings-as-errors flag `-W=error` was removed in
    # https://github.com/googleapis/proto-plus-python/pull/400.
    # It should be re-added once issue
    # https://github.com/protocolbuffers/protobuf/issues/12186 is fixed.
    session.run(
        "py.test",
        "--quiet",
        *(
            session.posargs  # Coverage info when running individual tests is annoying.
            or [
                "--cov=proto",
                "--cov-config=.coveragerc",
                "--cov-report=term",
                "--cov-report=html",
                "tests",
            ]
        ),
    )


# Check if protobuf has released wheels for new python versions
# https://pypi.org/project/protobuf/#files
# This list will generally be shorter than 'unit'
@nox.session(python=["3.6", "3.7", "3.8", "3.9", "3.10"])
def unitcpp(session):
    return unit(session, proto="cpp")


@nox.session(python=PYTHON_VERSIONS)
def unitupb(session):
    return unit(session, proto="upb")


@nox.session(python="3.9")
def docs(session):
    """Build the docs."""

    session.install("sphinx==4.2.0", "sphinx_rtd_theme")
    session.install(".")

    # Build the docs!
    session.run("rm", "-rf", "docs/_build/")
    session.run(
        "sphinx-build",
        "-W",
        "-b",
        "html",
        "-d",
        "docs/_build/doctrees",
        "docs/",
        "docs/_build/html/",
    )
