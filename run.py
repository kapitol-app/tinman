import src.utils.logger as logger
import src.db.db as db
from src.db.db_constants import Collections


def run():
    collections = Collections()
    target = {"currentParty": "D"}
    results = None
    try:
        results = db.find(collections.senators, target)
    except Exception as e:
        logger.error('Fetching', target)
    if results:
        [logger.log('result', result['firstName'], result['lastName']) for result in results]
