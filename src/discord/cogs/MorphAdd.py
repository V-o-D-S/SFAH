import disnake
from disnake import TextInputStyle
from disnake.ext import commands

import src.IDB.manage_morphs as manage_morph
import src.IDB.manage_servers as manage_servers
from src.config.commands import error_embed


class MorphsAdd(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.slash_command(name='morph_reg', description='Зарегистрировать морф в IDB')
	async def reg(self, ctx: disnake.AppCmdInter):
		role = manage_servers.get_manage_role(str(ctx.guild.id))
		member_role = ctx.author.get_role(int(role))

		if member_role is None:
			await ctx.send(embed=error_embed('Роль', 'У вас нет необходимой роли'))
			return 0

		await ctx.response.send_modal(modal=ModalMorph())
		await ctx.send(embed=disnake.Embed(
			title='Регистрация морфа!',
			description=f'Инспектор {ctx.author.mention} начал регистрацию пользовательского морфа',
			colour=disnake.Color.blurple()
		))


class ModalMorph(disnake.ui.Modal):
	def __init__(self):
		# Детали модального окна и его компонентов
		components = [
			disnake.ui.TextInput(
				label="ID",
				placeholder="Enter morph ID",
				custom_id="id",
				style=TextInputStyle.short,
				max_length=32,
			),
			disnake.ui.TextInput(
				label="Morph",
				placeholder="Enter morph",
				custom_id="morph",
				style=TextInputStyle.long,
				max_length=4000,
			),
			disnake.ui.TextInput(
				label="Player",
				placeholder="Enter Player ID (Bound)",
				custom_id="player",
				style=TextInputStyle.short,
				max_length=64,
			),
			disnake.ui.TextInput(
				label="Photo",
				placeholder="Enter Photo URL (https://[URL].png)",
				custom_id="photo",
				style=TextInputStyle.short,
				max_length=128
			),
			disnake.ui.TextInput(
				label="Structure",
				placeholder="Enter morph structure",
				custom_id="structure",
				style=TextInputStyle.short,
				max_length=32,
			),

		]
		super().__init__(
			title="System for Automatic Host",
			custom_id="system",
			components=components,
		)

	# Обработка ответа, после отправки модального окна
	async def callback(self, inter: disnake.ModalInteraction):
		data = inter.text_values
		data_send = {
			'id':        data['id'],
			'morph':     data['morph'],
			'inspector': str(inter.author.id),
			'bound':     data['player'],
			'photo':     data['photo'],
			'structure': data['structure']
		}
		if manage_morph.add_morph(data_send) == 0:
			await inter.channel.send(embed=disnake.Embed(
				title='Загрузка завершена!',
				description=f'Морф был загружен! Присвоен ID : {data_send["id"]}',
				color=disnake.Color.green()
			))
		else:
			await inter.channel.send(embed=error_embed('IDB', 'Failed load morph', -1))


def setup(bot):
	bot.add_cog(MorphsAdd(bot))
