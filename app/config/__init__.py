
#WTF_CSRF_ENABLED = True
REDIS_URL = "redis://crawler:Password@redis-17203.c10.us-east-1-4.ec2.cloud.redislabs.com:17203/alain-test-redis"
QUEUES = ["default"]

login_url = "http://extratoblubeapp-env.eba-mvegshhd.sa-east-1.elasticbeanstalk.com/login"
benefits_url = "http://extratoblubeapp-env.eba-mvegshhd.sa-east-1.elasticbeanstalk.com/offline/listagem"
headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Host": "extratoblubeapp-env.eba-mvegshhd.sa-east-1.elasticbeanstalk.com",
            "Origin": "http://ionic-application.s3-website-sa-east-1.amazonaws.com",
            "Referer": "http://ionic-application.s3-website-sa-east-1.amazonaws.com/",
            "Referrer Policy": "strict-origin-when-cross-origin",
            "Accept-Language": "es,pt;q=0.9,pt-BR;q=0.8,en;q=0.7",
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 1(KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
main_page = "http://extratoclube.com.br"
