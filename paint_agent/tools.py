"""Tools для root_agent: запись значений в state сессии."""

from google.adk.tools.tool_context import ToolContext


def set_session_value(key: str, value: str, tool_context: ToolContext) -> str:
    """Сохраняет значение в state сессии, чтобы другие агенты могли его использовать.

    Args:
        key: Имя ключа, например PRICE или COVERAGE_RATE.
        value: Значение, которое нужно сохранить. Только число без единиц измерения.

    Returns:
        Подтверждение записи.
    """
    tool_context.state[key] = value
    return f"stored '{value}' in '{key}'"
