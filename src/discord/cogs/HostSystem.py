import disnake
from disnake.ext import commands


class HostSystem(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(name='host_info', description='Получить информацию о хосте')
	async def host_info(self, ctx: disnake.AppCmdInter):
		await ctx.send(embed=disnake.Embed(
			title='Информация | ⚫',
			description='На данный момент авто хост не запущен.',
			color=disnake.Colour.dark_red()
		))


def setup(bot):
	bot.add_cog(HostSystem(bot))
