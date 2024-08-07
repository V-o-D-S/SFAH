import disnake
from disnake.ext import commands

import src.IDB.manage_servers as manage_servers
from src.config.commands import error_embed

DEV_SERVER = 1227280685526552656
DEV_ROLE = 1227479238601605201


class ServerManager(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(name='server_reg', description='Зарегистрировать сервер')
	async def reg(self, ctx: disnake.AppCmdInter):
		dev_guild = ctx.client.get_guild(DEV_SERVER)
		role = dev_guild.get_role(DEV_ROLE)

		member = ctx.author
		if member in dev_guild.members:
			if member in role.members:
				manage_servers.server_registration(str(ctx.guild.id))
				embed = disnake.Embed(
					title='Сервер зарегистрирован!',
					description=f'Сервер {ctx.guild.name} был зарегистрирован!',
					color=disnake.Color.green()
				)
				await ctx.send(embed=embed)
			else:
				await ctx.send(embed=error_embed(title='Forbidden', note='You cant use this command', code=2))
		else:
			await ctx.send(embed=error_embed(title='Forbidden', note='You cant use this command', code=1))

	@commands.slash_command(name='server_unreg', description='Удалить сервер')
	async def unreg(self, ctx: disnake.AppCmdInter, identifier_server):
		dev_guild = ctx.client.get_guild(DEV_SERVER)
		role = dev_guild.get_role(DEV_ROLE)

		member = ctx.author
		if member in dev_guild.members:
			if member in role.members:
				manage_servers.server_unregistration(str(ctx.guild.id))
				embed = disnake.Embed(
					title='Сервер зарегистрирован!',
					description=f'Сервер {ctx.guild.name} был удален!',
					color=disnake.Color.green()
				)
				await ctx.send(embed=embed)
			else:
				await ctx.send(embed=error_embed(title='Forbidden', note='You cant use this command', code=2))
		else:
			await ctx.send(embed=error_embed(title='Forbidden', note='You cant use this command', code=1))

	@commands.slash_command(name='add_manage_role', description='Изменить роль менеджера. (Ничего если удалить)')
	async def add_manage_role(self, ctx: disnake.AppCmdInter, identifier_role='nothing'):
		dev_guild = ctx.client.get_guild(DEV_SERVER)
		role = dev_guild.get_role(DEV_ROLE)

		member = ctx.author
		if member in dev_guild.members:
			if member in role.members:
				manage_servers.upd_manage_role(str(ctx.guild.id), identifier_role)
				embed = disnake.Embed(
					title='Сервер зарегистрирован!',
					description=f'Роль <@&{identifier_role}> была зарегистрирована для сервера {ctx.guild.name}!',
					color=disnake.Color.green()
				)
				await ctx.send(embed=embed)
			else:
				await ctx.send(embed=error_embed(title='Forbidden', note='You cant use this command', code=2))
		else:
			await ctx.send(embed=error_embed(title='Forbidden', note='You cant use this command', code=1))


def setup(bot):
	bot.add_cog(ServerManager(bot))
