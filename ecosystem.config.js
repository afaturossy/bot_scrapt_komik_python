module.exports = {
  apps : [{
    name   : "scrapt-komikindo.info",
    script : "/home/website/komikindo.info_copy/bot_scrapt_komik_python/komikindo.info/main.py",
    interpreter : "/home/website/komikindo.info_copy/bot_scrapt_komik_python/venv/bin/python",
    autorestart: false,
   cron_restart: '0 * * * *'
  }]
}
