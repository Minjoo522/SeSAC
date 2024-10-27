import logging
import argparse

logger = logging.getLogger('my-logger')

# 로그레벨 설정
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.WARNING)

# 로그 포멧팅
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 터미널에 출력하는 핸들러
handler1 = logging.StreamHandler()

# 파일에 쓰는 핸들러
handler2 = logging.FileHandler('my-log.log')
handler1.setFormatter(formatter)
handler2.setFormatter(formatter)
logger.addHandler(handler1)
logger.addHandler(handler2)

# default 핸들러 없애기
logger.propagate = False
# ✨ 결과
# 2023-08-21 13:42:00,959 - my-logger = WARNING - 헬로우3
# 2023-08-21 13:42:00,959 - my-logger = ERROR - 헬로우2
# 2023-08-21 13:42:00,959 - my-logger = CRITICAL - 헬로우1

# 로그 옵션 동적 처리
parser = argparse.ArgumentParser()
# 실행할 때 python mylog.py -d DEBUG 이런식으로!
parser.add_argument('-d', '--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='INFO', help='로그레벨설정')
args = parser.parse_args()

# 로그 레벨 적용
log_level_args = args.log_level.upper()
logger.setLevel(log_level_args)

# 로그를 출력하는 방법
# 밑으로 갈수록 심각하고 중요!
logger.debug('헬로우5')
logger.info('헬로우4')
logger.warning('헬로우3')
logger.error('헬로우2')
logger.critical('헬로우1')

# 너무 디테일하게 넣어놓는 것은 좋지 않음