from __future__ import annotations

from textwrap import dedent

import pytest  # FORK_DISABLE_MAYBE

import strawberry
from strawberry import Maybe

pytest.skip("Maybe disabled in fork", allow_module_level=True)  # FORK_DISABLE_MAYBE


def test_maybe_annotation_from_strawberry():
    global MyInput
    try:

        @strawberry.input
        class MyInput:
            my_value: strawberry.Maybe[str]

        @strawberry.type
        class Query:
            @strawberry.field
            def test(self, my_input: MyInput) -> str:
                return "OK"

        schema = strawberry.Schema(query=Query)
        expected_schema = dedent("""
        input MyInput {
          myValue: String
        }

        type Query {
          test(myInput: MyInput!): String!
        }
        """).strip()
        assert str(schema) == expected_schema

        assert MyInput()
    finally:
        del MyInput


def test_maybe_annotation_directly():
    global MyInput
    try:

        @strawberry.input
        class MyInput:
            my_value: Maybe[str]

        @strawberry.type
        class Query:
            @strawberry.field
            def test(self, my_input: MyInput) -> str:
                return "OK"

        schema = strawberry.Schema(query=Query)
        expected_schema = dedent("""
        input MyInput {
          myValue: String
        }

        type Query {
          test(myInput: MyInput!): String!
        }
        """).strip()
        assert str(schema) == expected_schema

        assert MyInput()
    finally:
        del MyInput
