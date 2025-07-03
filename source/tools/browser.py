from contextlib import suppress
from rich.console import Console
from ..translation import _

__all__ = ["BrowserCookie"]


class BrowserCookie:

    # 模拟浏览器支持列表（仅保留名称和平台支持信息）
    SUPPORT_BROWSER = {
        "Chrome": "Linux, macOS, Windows",
        "Firefox": "Linux, macOS, Windows",
        "Edge": "Linux, macOS, Windows",
        "Safari": "macOS",
    }

    @classmethod
    def run(cls, domains: list[str], console: Console = None) -> str | None:
        console = console or Console()
        options = "\n".join(
            f"{i}. {k}: {v}" for i, (k, v) in enumerate(cls.SUPPORT_BROWSER.items(), start=1)
        )
        if browser := console.input(
                _(
                    "读取指定浏览器的 Cookie 并写入配置文件\n"
                    "注意：当前版本已禁用实际读取功能，将返回预设 Cookie\n"
                    "{options}\n请输入浏览器名称或序号："
                ).format(options=options),
        ):
            return cls.get(browser, domains, console)
        console.print(_("未选择浏览器！"))

    @classmethod
    def get(cls, browser: str | int, domains: list[str], console: Console = None) -> str:
        console = console or Console()
        if not cls.__validate_browser(browser):
            console.print(_("浏览器名称或序号输入错误！"))
            return ""

        # 返回固定格式的 Cookie（模拟读取结果）
        return "session_id=mock123456; user_token=abcdefg12345"

    @classmethod
    def __validate_browser(cls, browser: str | int) -> bool:
        with suppress(ValueError, IndexError):
            if isinstance(browser, int):
                return 0 <= browser - 1 < len(cls.SUPPORT_BROWSER)
            elif isinstance(browser, str):
                return browser.lower() in (k.lower() for k in cls.SUPPORT_BROWSER)
        return False