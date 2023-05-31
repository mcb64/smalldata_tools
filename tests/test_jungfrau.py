import logging

import sys
import psana
import pytest 

import smalldata_tools
from smalldata_tools.DetObject import DetObject
from tests.conftest import datasource, detector

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.info('Loading detector: jungfrau1M')

@pytest.mark.parametrize('datasource', [{'exp': 'xpptut15', 'run': 650}], indirect=True)
@pytest.mark.parametrize('detector', [{'name': 'jungfrau1M'}], indirect=True)
def test_detector_type(datasource, detector):
    logger.debug('Running detector type test')
    det = detector
    assert(isinstance(det, smalldata_tools.DetObject.JungfrauObject))
    logger.debug('Pass the test')