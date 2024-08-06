import disnake


def error_embed(title, note, code = 0):
	return disnake.Embed(title=f"Ошибка! {title}",
						 description=f"Ошибка! Пояснение к ошибке: {note}. Error Code: {code}",
						 color=disnake.Color.red())
