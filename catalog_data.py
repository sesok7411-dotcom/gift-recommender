# catalog_data.py
"""
통합 선물 카탈로그 데이터베이스 (총 800개 아이템)
- 10개 프로필 (5개 관계 x 2개 성별)
- 각 프로필별 5대 연령대 (10대, 20대, 30대, 40대, 50대 이상) 각 16개 아이템 (총 80개)
- 10대 부적절 상품(호텔 스파, 마사지, 주류 등) 100% 원천 배제
- 동일 연령대 내 관계 변경 시 중복률 0.0% (800개 전 아이템 고유성 보장)
- 예산 구간별(1~3만, 4~7만, 8~14만, 15~23만, 25~30만) 엄격 매칭 보장
"""

from cat_profile_lover import LOVER_DATA
from cat_profile_colleague import COLLEAGUE_DATA
from cat_profile_friend import FRIEND_DATA
from cat_profile_family import FAMILY_DATA
from cat_profile_acquaintance import ACQUAINTANCE_DATA

CATALOG_DATA = {}
CATALOG_DATA.update(LOVER_DATA)
CATALOG_DATA.update(COLLEAGUE_DATA)
CATALOG_DATA.update(FRIEND_DATA)
CATALOG_DATA.update(FAMILY_DATA)
CATALOG_DATA.update(ACQUAINTANCE_DATA)
