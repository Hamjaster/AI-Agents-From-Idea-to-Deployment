"""Deterministic calculator tool for quick quantitative reasoning."""
from __future__ import annotations

import ast
import operator
from typing import Any, Dict

from langchain.tools import BaseTool
from langchain_core.callbacks import CallbackManagerForToolRun

_ALLOWED_OPERATORS: Dict[type[ast.AST], Any] = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


class CalculatorTool(BaseTool):
    name = "deterministic_calculator"
    description = (
        "Perform precise arithmetic on simple expressions. "
        "Supports addition, subtraction, multiplication, division, modulus, and powers."
    )

    def _run(
        self,
        query: str,
        run_manager: CallbackManagerForToolRun | None = None,  # noqa: ARG002 - standard signature
    ) -> str:
        try:
            expression = ast.parse(query, mode="eval").body
            result = self._eval(expression)
            return str(result)
        except Exception as exc:  # pragma: no cover - defensive layer
            raise ValueError(f"Failed to evaluate expression '{query}': {exc}") from exc

    async def _arun(
        self,
        query: str,
        run_manager: CallbackManagerForToolRun | None = None,
    ) -> str:  # pragma: no cover - async interface not required for workshop
        raise NotImplementedError("CalculatorTool does not support async execution.")

    def _eval(self, node: ast.AST) -> float:
        if isinstance(node, ast.Num):  # type: ignore[attr-defined]
            return float(node.n)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)
        if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED_OPERATORS:
            return _ALLOWED_OPERATORS[type(node.op)](self._eval(node.operand))
        if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_OPERATORS:
            left = self._eval(node.left)
            right = self._eval(node.right)
            return _ALLOWED_OPERATORS[type(node.op)](left, right)
        raise ValueError(f"Unsupported expression: {ast.dump(node, include_attributes=False)}")
