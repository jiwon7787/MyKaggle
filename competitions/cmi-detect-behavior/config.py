from pathlib import Path
PROJECT = Path(__file__).resolve().parents[0]
DATA = PROJECT / "data"
RAW = DATA / "raw"
PROCESSED = DATA / "processed"

# Kaggle公式データ（ローカルに配置/リンク済み想定）
RAW_DIR = RAW / "cmi-detect-behavior-with-sensor-data"

# 追加の事前学習物（ない場合は None のまま）
PRETRAINED_DIR = None  # 例: (PROJECT / "data" / "cmi-d-111")
