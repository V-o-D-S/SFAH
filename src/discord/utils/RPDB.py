import pkgutil

import disnake
from disnake.ext import commands


class RPDBBot(commands.InteractionBot):
	def __init__(self):
		super().__init__(
			intents=disnake.Intents.all(),
			test_guilds=[1227280685526552656,1247566813500543099]
		)

	async def on_ready(self):
		print(f'Logged in as {self.user}')
		print(disnake.__version__)

	def load_cog(self, path: str):
		for file in pkgutil.iter_modules([path]):
			try:
				self.load_extension(f'cogs.{file.name}')
				print(f'Loaded {file.name}')
			except Exception as e:
				print(f'Failed to load {file.name} ({e})')
			# print(f'Failed to load {file.name} ({type(e).__name__} (FULL IN log.txt))')
