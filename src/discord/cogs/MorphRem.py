import disnake
from disnake.ext import commands

import src.IDB.manage_morphs as manage_morph
import src.IDB.manage_servers as manage_servers
from src.config.commands import error_embed


class MorphsRemove(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(name='morph_unreg', description='Удалить морф из IDB')
	async def unreg(self, ctx: disnake.AppCmdInter, identifier):
		role = manage_servers.get_manage_role(str(ctx.guild.id))
		member_role = ctx.author.get_role(int(role))

		if member_role is None:
			await ctx.send(embed=error_embed('Роль', 'У вас нет необходимой роли'))
			return 0

		morph = manage_morph.find_morph(identifier)
		if morph == -1 or morph is None:
			await ctx.send(embed=error_embed('Morph', 'morph not found'))
			return 0
		else:
			code = manage_morph.del_morph(identifier)
			if code == 0:
				await ctx.send(embed=disnake.Embed(
					title='Готово!',
					description=f'Морф {identifier} был успешно удален!',
					color=disnake.Color.green()
				))
			else:
				await ctx.send(embed=error_embed('DataBase', 'Morph not deleted'))


def setup(bot):
	bot.add_cog(MorphsRemove(bot))
