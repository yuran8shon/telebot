class SoSyslog:
	def events(self):
		# @todo #40 Необходимо получить список событий, которые возникли с момента
		#  последнего обращения. Не знаю точно, что мы хотим там увидеть, Давайте для начала
		#  найдет все события от systemd и вернем их в виде событий.
		return []