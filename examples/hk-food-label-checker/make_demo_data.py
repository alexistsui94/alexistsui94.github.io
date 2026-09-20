# confidentiality: public-approved
"""Build an entirely synthetic workbook. No customer knowledge is distributed."""
from pathlib import Path
import argparse
import pandas as pd


def make_demo(destination: Path) -> None:
    master = pd.DataFrame([
        {'additive_id': 'DEMO001', 'canonical_name_zh_cn': '演示成分甲',
         'canonical_name_zh_hk': '演示成分甲', 'canonical_name_en': 'Demo ingredient A',
         'e_number': 'DEMO-001', 'e_number_norm': 'DEMO-001',
         'function_zh_cn': '虚构演示功能', 'function_zh_hk': '虛構演示功能',
         'function_en': 'Synthetic demonstration only', 'notes': '虚构记录，不是食品法规或添加剂依据'},
        {'additive_id': 'DEMO002', 'canonical_name_zh_cn': '演示成分乙',
         'canonical_name_zh_hk': '演示成分乙', 'canonical_name_en': 'Demo ingredient B',
         'e_number': 'DEMO-002', 'e_number_norm': 'DEMO-002',
         'function_zh_cn': '虚构演示功能', 'function_zh_hk': '虛構演示功能',
         'function_en': 'Synthetic demonstration only', 'notes': '虚构记录，不是食品法规或添加剂依据'},
    ])
    aliases = pd.DataFrame([
        {'alias_text': '测试别名A', 'alias_type': 'demo', 'additive_id': 'DEMO001', 'is_fuzzy_candidate': False},
        {'alias_text': '测试别名B', 'alias_type': 'demo', 'additive_id': 'DEMO002', 'is_fuzzy_candidate': False},
    ])
    common = pd.DataFrame([{'name': '水', 'name_norm': '水'}, {'name': '白砂糖', 'name_norm': '白砂糖'}])
    with pd.ExcelWriter(destination, engine='openpyxl') as writer:
        master.to_excel(writer, sheet_name='additives_master', index=False)
        aliases.to_excel(writer, sheet_name='additives_aliases', index=False)
        common.to_excel(writer, sheet_name='common_non_additives', index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('demo_knowledge.xlsx'))
    args = parser.parse_args()
    if args.output.exists():
        parser.error('Output already exists; choose a new path to preserve existing data.')
    make_demo(args.output)
    print(f'Created synthetic data: {args.output.name}')

