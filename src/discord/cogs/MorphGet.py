import disnake
from disnake.ext import commands

import src.IDB.manage_morphs as manage_morphs
from src.config.commands import error_embed


class MorphGet(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(name='morph_get', description='Зарегистрировать морф в IDB')
	async def get(self, ctx: disnake.AppCmdInter, identifier):
		data = manage_morphs.find_morph(identifier)
		if data in [-1, None]:
			await ctx.send(embed=error_embed('Морф!', 'Морф не найден, или была получена ошибка'))
		else:
			embed = disnake.Embed(
				title=f'Морф {identifier}',
				description=f'Данные морфа {identifier} получены.',
				color=disnake.Color.green()
			)
			embed.add_field(name='ID', value=identifier)
			embed.add_field(name='Morph', value=data[1], inline=False)
			embed.add_field(name='Inspector', value=f'<@{data[2]}>')
			embed.add_field(name='Player bound', value=f'<@{data[3]}>')
			embed.add_field(name='Structure', value=data[5])

			embed.set_image(url=data[4])
			await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(MorphGet(bot))
