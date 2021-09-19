import asyncio
from typing import Optional

from .http import Http
from .models import UserProfile
from .errors import NotPremium
from .helpers import Xbox, Microsoft

__all__ = ("MsMcAuth",)

class MsMcAuth:
    """"Microsoft Minecraft Auth Client.

    Attributes
    ----------
    loop : Optional[:class:`asyncio.ProactorEventLoop`]
        Asyncio loop. Default: :class:`asyncio.ProactorEventLoop`
    """

    def __init__(self, *, loop: Optional[asyncio.ProactorEventLoop] = None):
        self.loop = loop or asyncio.get_event_loop()
        self.http = Http(loop=self.loop)

    async def login(self, email: str, password: str) -> UserProfile:
        xbox = Xbox(http=self.http)
        microsoft = Microsoft(http=self.http)

        _login = await xbox.xbox_login(email, password, (await xbox.get_pre_auth()))

        xbl = await microsoft.handle_xbl(_login)
        xsts = await microsoft.handle_xsts(xbl)

        access_token = await microsoft.login_with_xbox(xsts)
        has_the_game = await microsoft.user_hash_game(access_token)

        if has_the_game:
            return await microsoft.get_minecraft_profile(access_token)

        raise NotPremium("Account is not premium.")

