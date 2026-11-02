# -*- coding: utf-8 -*-
"""
HỆ CHUYÊN GIA TƯ VẤN LỰA CHỌN MUA ĐIỆN THOẠI DI ĐỘNG
Xây dựng dựa trên file báo cáo BT(1).docx và cấu trúc giao diện của hoan.py.
Chạy bằng: streamlit run dien_thoai_app.py
"""
import streamlit as st
from pathlib import Path

# Thu muc images nam cung cap voi file bandt2.py
IMAGE_DIR = Path(__file__).parent / "images"

def get_phone_image(phone_id):
    """Tim anh san pham theo ma D1, D2... trong thu muc images."""
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        image_path = IMAGE_DIR / f"{phone_id}{ext}"
        if image_path.exists():
            return str(image_path)
    return None

st.set_page_config(page_title="Hệ chuyên gia tư vấn mua điện thoại",
                   page_icon="📱", layout="wide")

# Giao dien moi: sac so, vui tuoi; chi thay doi phan trinh bay, khong sua noi dung/logic tu van.
st.markdown("""
<style>
:root {
  --ink: #242052;
  --pink: #ff4f9a;
  --purple: #7857ff;
  --cyan: #23c9d8;
  --yellow: #ffd166;
}
.stApp {
  background:
    radial-gradient(ellipse at 8% 8%, rgba(255,79,154,.20), transparent 26%),
    radial-gradient(ellipse at 92% 18%, rgba(35,201,216,.20), transparent 25%),
    radial-gradient(ellipse at 80% 88%, rgba(120,87,255,.16), transparent 28%),
    linear-gradient(135deg, #fff8fd 0%, #f4f6ff 48%, #f0fdff 100%);
  color: var(--ink);
}
.block-container { max-width: 1250px; padding-top: 2.1rem; padding-bottom: 3rem; }
/* Hieu ung hoa tiet cham nho tren nen */
.stApp:before {
  content: "✦  ✧     •      ✦        ✧       •";
  position: fixed; top: 7px; right: 4%; z-index: 0; pointer-events: none;
  color: rgba(120,87,255,.25); font-size: 27px; letter-spacing: 15px;
}
h1 {
  color: #5b35d5 !important; font-weight: 900 !important;
  letter-spacing: -.7px; line-height: 1.22 !important;
  background: linear-gradient(90deg, #6b3df4, #f0449a 52%, #119fb7);
  -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
}
h2, h3 { color: #4b36a8 !important; font-weight: 800 !important; }
[data-testid="stCaptionContainer"] { color: #716b98; }
/* Khung tu van va the san pham */
[data-testid="stVerticalBlockBorderWrapper"] {
  border: 1px solid rgba(135,105,235,.24) !important;
  border-radius: 22px !important;
  background: rgba(255,255,255,.86) !important;
  box-shadow: 0 10px 28px rgba(82,60,155,.09);
  transition: transform .2s ease, box-shadow .2s ease;
}
[data-testid="stVerticalBlockBorderWrapper"]:hover {
  box-shadow: 0 14px 32px rgba(82,60,155,.15);
}
[data-testid="stSelectbox"] label, [data-testid="stWidgetLabel"] {
  color: #4b3c89 !important; font-weight: 700 !important;
}
[data-baseweb="select"] > div {
  border: 1.5px solid #ded5ff !important; border-radius: 12px !important;
  background: #fff !important;
}
[data-baseweb="select"] > div:focus-within {
  border-color: #8b63ff !important; box-shadow: 0 0 0 3px rgba(139,99,255,.12);
}
.stButton > button {
  border: 0 !important; border-radius: 14px !important;
  background: linear-gradient(100deg, #7652f6, #f14b9a 58%, #ff8b62) !important;
  color: white !important; font-weight: 800 !important;
  box-shadow: 0 7px 18px rgba(217,71,164,.25);
  transition: transform .18s ease, box-shadow .18s ease;
}
.stButton > button:hover { transform: translateY(-2px); box-shadow: 0 11px 24px rgba(217,71,164,.32); }
[data-testid="stAlert"] { border-radius: 15px !important; border-width: 1px !important; }
[data-testid="stExpander"] { border: 1px solid #e4dcff; border-radius: 14px; background: #fcfaff; }
hr { border-color: rgba(130,105,220,.22) !important; }
[data-testid="stImage"] img { border-radius: 16px; border: 1px solid #eee7ff; }
/* Thong tin ket qua de doc, giu nguyen toan bo chu va du lieu */
[data-testid="stMarkdownContainer"] p { line-height: 1.65; }
@media (max-width: 700px) {
  .block-container { padding-top: 1rem; padding-left: 1rem; padding-right: 1rem; }
  h1 { font-size: 1.75rem !important; }
}
</style>
""", unsafe_allow_html=True)

PHONES = [
    {
        "id": "D1",
        "name": "iPhone 15",
        "brand": "Apple",
        "storage": "128GB, 256GB, 512GB",
        "camera": "48MP",
        "needs": "Gaming tốt, Chụp ảnh – quay phim",
        "battery": "Dưới 4000mAh ( Pin sản phẩm 3349 mAh )",
        "charging": "Sạc nhanh (20W)",
        "screen": "Màn đẹp ( OLED )",
        "chip": "Apple A17",
        "ram": "6GB",
        "water": "Kháng tốt ( IP68 )",
        "description": "Sự kết hợp cân bằng giữa kích thước nhỏ gọn (6.1 inch), trọng lượng nhẹ và mức giá dễ tiếp cận nhất. Máy đáp ứng trọn vẹn mọi nhu cầu sử dụng hàng ngày từ giải trí, chụp ảnh đến làm việc.",
        "variants": [
            {
                "ram": "6GB",
                "storage": "128GB",
                "price": 17290000,
                "price_band": "15–20 triệu"
            },
            {
                "ram": "6GB",
                "storage": "256GB",
                "price": 20590000,
                "price_band": "20–25 triệu"
            },
            {
                "ram": "6GB",
                "storage": "512GB",
                "price": 23990000,
                "price_band": "20–25 triệu"
            }
        ]
    },
    {
        "id": "D2",
        "name": "iPhone 15 Plus",
        "brand": "Apple",
        "storage": "128GB, 256GB, 512GB",
        "camera": "48MP",
        "needs": "Gaming tốt, Chụp ảnh – quay phim",
        "battery": "Từ 4000 đến 5000 mAh ( Pin sản phẩm 4383 mAh )",
        "charging": "Sạc nhanh (20W)",
        "screen": "Màn đẹp ( OLED )",
        "chip": "Apple A17",
        "ram": "6GB",
        "water": "Kháng tốt ( IP68 )",
        "description": "Giữ nguyên cấu hình của iPhone 15 nhưng mang thiết kế lớn hơn (6.7 inch). Đây là lựa chọn tối ưu cho người thích không gian hiển thị rộng rãi để xem phim, chơi game và ưu tiên thời lượng pin vượt trội.",
        "variants": [
            {
                "ram": "6GB",
                "storage": "128GB",
                "price": 19590000,
                "price_band": "15–20 triệu"
            },
            {
                "ram": "6GB",
                "storage": "256GB",
                "price": 22590000,
                "price_band": "20–25 triệu"
            },
            {
                "ram": "6GB",
                "storage": "512GB",
                "price": 27990000,
                "price_band": "25–30 triệu"
            }
        ]
    },
    {
        "id": "D3",
        "name": "iPhone 16e",
        "brand": "Apple",
        "storage": "128GB, 512GB",
        "camera": "48MP",
        "needs": "Gaming tốt, Chụp ảnh – quay phim",
        "battery": "Từ 4000 đến 5000 mAh ( Pin sản phẩm 4005 mAh )",
        "charging": "Sạc nhanh (20W)",
        "screen": "Màn đẹp ( OLED )",
        "chip": "Apple A",
        "ram": "8GB",
        "water": "Kháng tốt ( IP68 )",
        "description": "iPhone 16e vừa gia nhập đại gia đình iPhone của Apple, với thiết kế tinh gọn và hiệu suất xử lý ấn tượng. Mẫu điện thoại này có giá phải chăng, tích hợp Apple Intelligence và tính năng AI thông minh, hứa hẹn mang đến trải nghiệm thú vị cho người dùng.",
        "variants": [
            {
                "ram": "8GB",
                "storage": "128GB",
                "price": 14990000,
                "price_band": "10–15 triệu"
            },
            {
                "ram": "8GB",
                "storage": "512GB",
                "price": 23990000,
                "price_band": "20–25 triệu"
            }
        ]
    },
    {
        "id": "D4",
        "name": "16",
        "brand": "Apple",
        "storage": "128GB",
        "camera": "48MP",
        "needs": "Gaming tốt, Chụp ảnh – quay phim",
        "battery": "Dưới 4000 mAh (Pin sản phẩm 3582 mAh)",
        "charging": "Sạc nhanh (20W)",
        "screen": "Màn đẹp ( OLED )",
        "chip": "Apple A18",
        "ram": "8GB",
        "water": "Kháng tốt ( IP68 )",
        "description": "Nâng cấp tập trung vào phím bấm vật lý mới (Camera Control, Nút Action), vi xử lý thế hệ mới hỗ trợ các tính năng AI thông minh và thiết kế cụm camera dọc hiện đại hơn.",
        "variants": [
            {
                "ram": "8GB",
                "storage": "128GB",
                "price": 21290000,
                "price_band": "20–25 triệu"
            }
        ]
    },
    {
        "id": "D5",
        "name": "16 Plus",
        "brand": "Apple",
        "storage": "128GB, 256GB, 512GB",
        "camera": "48MP",
        "needs": "Gaming tốt, Chụp ảnh – quay phim",
        "battery": "Từ 4000 đến 5000 mAh (Pin sản phẩm 4674 mAh)",
        "charging": "Sạc nhanh (20W)",
        "screen": "Màn đẹp ( OLED )",
        "chip": "Apple A18",
        "ram": "8GB",
        "water": "Kháng tốt ( IP68 )",
        "description": "Bản phóng to của iPhone 16 với màn hình 6.7 inch. Giữ trọn ưu điểm pin \"trâu\" và màn to của dòng Plus, kết hợp cùng cụm camera dọc hoàn toàn mới, cặp nút bấm tiện lợi (Action & Camera Control) và chip A18 hỗ trợ tính năng AI thông minh. Lựa chọn tuyệt vời cho ai thích máy to, pin xài thả ga mà vẫn muốn trải nghiệm công nghệ mới nhất.",
        "variants": [
            {
                "ram": "8GB",
                "storage": "128GB",
                "price": 25090000,
                "price_band": "25–30 triệu"
            },
            {
                "ram": "8GB",
                "storage": "256GB",
                "price": 28590000,
                "price_band": "25–30 triệu"
            },
            {
                "ram": "8GB",
                "storage": "512GB",
                "price": 30090000,
                "price_band": "30–35 triệu"
            }
        ]
    },
    {
        "id": "D6",
        "name": "16 Pro",
        "brand": "Apple",
        "storage": "128GB, 256GB, 1TB",
        "camera": "48MP",
        "needs": "Gaming tốt, Chụp ảnh – quay phim",
        "battery": "Từ 4000 đến 5000 mAh (Pin sản phẩm 4582 mAh)",
        "charging": "Sạc nhanh (20W)",
        "screen": "Màn đẹp ( OLED )",
        "chip": "Apple A18",
        "ram": "8GB",
        "water": "Kháng tốt ( IP68 )",
        "description": "Với sự ra mắt bùng nổ của phiên bản iPhone 16, Apple đã tiếp tục khẳng định vị thế của mình trong thị trường điện thoại thông minh bằng những cải tiến mang tính cách mạng. Sở hữu thiết kế tinh tế, công nghệ tiên tiến và hiệu năng vượt trội đã làm cho iPhone 16 Pro trở thành một trong những sản phẩm công nghệ đáng chú ý nhất năm, mang đến cho người dùng trải nghiệm tương lai trong tầm tay.",
        "variants": [
            {
                "ram": "8GB",
                "storage": "256GB",
                "price": 24990000,
                "price_band": "20–25 triệu"
            },
            {
                "ram": "8GB",
                "storage": "512GB",
                "price": 28590000,
                "price_band": "25–30 triệu"
            },
            {
                "ram": "8GB",
                "storage": "128GB, 256GB, 1TB",
                "price": 39990000,
                "price_band": "35–40 triệu"
            }
        ]
    },
    {
        "id": "D7",
        "name": "16 Pro Max",
        "brand": "Apple",
        "storage": "256GB, 512GB",
        "camera": "48MP",
        "needs": "Gaming tốt, Chụp ảnh – quay phim",
        "battery": "Từ 4000 đến 5000 mAh (Pin sản phẩm 4685 mAh)",
        "charging": "Sạc nhanh (20W)",
        "screen": "Màn đẹp ( OLED )",
        "chip": "Apple A18Pro",
        "ram": "8GB",
        "water": "Kháng tốt ( IP68 )",
        "description": "Mẫu flagship cao cấp nhất thế thế hệ 16 với màn hình cực lớn 6.9 inch, viền siêu mỏng và thời lượng pin trâu nhất lịch sử iPhone. Máy sở hữu khung viền Titanium sang trọng, cụm camera Pro đỉnh cao với zoom quang học 5x, nút bấm Camera Control tiện lợi cùng chip A18 Pro mạnh mẽ nhất để cân mọi tác vụ nặng và công nghệ AI. Lựa chọn tuyệt vời cho ai muốn sở hữu chiếc iPhone hoàn hảo nhất về cả hiệu năng, nhiếp ảnh lẫn thời lượng pin.",
        "variants": [
            {
                "ram": "8GB",
                "storage": "256GB",
                "price": 30590000,
                "price_band": "30–35 triệu"
            },
            {
                "ram": "8GB",
                "storage": "512GB",
                "price": 36990000,
                "price_band": "35–40 triệu"
            }
        ]
    },
    {
        "id": "D8",
        "name": "iPhone 17",
        "brand": "Apple",
        "storage": "512GB",
        "camera": "48MP",
        "needs": "Gaming tốt, Chụp ảnh – quay phim",
        "battery": "Dưới 4000 mAh (Pin sản phẩm 3692 mAh)",
        "charging": "Sạc nhanh (40W)",
        "screen": "Màn đẹp ( OLED )",
        "chip": "Apple A19",
        "ram": "8GB",
        "water": "Kháng tốt ( IP68 )",
        "description": "Sự nâng cấp toàn diện cho nhu cầu cơ bản với màn hình nhỏ gọn, thiết kế hiện đại, camera cải tiến và hiệu năng mượt mà. Máy đáp ứng trọn vẹn mọi tác vụ hàng ngày với mức giá dễ tiếp cận nhất trong thế hệ 17.",
        "variants": [
            {
                "ram": "8GB",
                "storage": "512GB",
                "price": 31490000,
                "price_band": "30–35 triệu"
            }
        ]
    },
    {
        "id": "D9",
        "name": "iphone 17 Pro",
        "brand": "Apple",
        "storage": "256GB, 512GB, 1TB",
        "camera": "48MP",
        "needs": "Cấu hình khủng, Chụp ảnh – quay phim",
        "battery": "Dưới 4000 mAh (Pin sản phẩm 3998 mAh)",
        "charging": "Sạc nhanh (40W)",
        "screen": "Màn đẹp ( OLED )",
        "chip": "Apple A19 Pro",
        "ram": "12GB",
        "water": "Kháng tốt ( IP68 )",
        "description": "Phiên bản hội tụ đầy đủ công nghệ đỉnh cao như cụm camera Pro chuyên nghiệp, chip xử lý mạnh mẽ nhất và chất liệu hoàn thiện cao cấp, dành cho người muốn trải nghiệm tính năng Pro nhưng thích kích thước vừa tay.",
        "variants": [
            {
                "ram": "12GB",
                "storage": "256GB",
                "price": 34990000,
                "price_band": "30–35 triệu"
            },
            {
                "ram": "12GB",
                "storage": "512GB",
                "price": 41490000,
                "price_band": "40–45 triệu"
            },
            {
                "ram": "12GB",
                "storage": "256GB, 512GB, 1TB",
                "price": 47990000,
                "price_band": "45–50 triệu"
            }
        ]
    },
    {
        "id": "D10",
        "name": "17 Pro Max",
        "brand": "Apple",
        "storage": "256GB, 512GB, 2TB",
        "camera": "48MP",
        "needs": "Cấu hình khủng, Chụp ảnh – quay phim",
        "battery": "Từ 4000 đến 5000 mAh (Pin sản phẩm 4823 mAh)",
        "charging": "Sạc nhanh (40W)",
        "screen": "Màn đẹp ( OLED )",
        "chip": "Apple A",
        "ram": "12GB",
        "water": "Kháng tốt ( IP68 )",
        "description": "Giữ trọn cấu hình mạnh mẽ của bản Pro nhưng sở hữu màn hình rộng rãi nhất và thời lượng pin vượt trội. Đây là lựa chọn hàng đầu cho người dùng muốn sở hữu những gì tốt nhất: xem phim, chơi game đỉnh cao và chụp ảnh/quay phim chuyên nghiệp.",
        "variants": [
            {
                "ram": "12GB",
                "storage": "256GB",
                "price": 37990000,
                "price_band": "35–40 triệu"
            },
            {
                "ram": "12GB",
                "storage": "512GB",
                "price": 44490000,
                "price_band": "40–45 triệu"
            },
            {
                "ram": "12GB",
                "storage": "256GB, 512GB, 2TB",
                "price": 63990000,
                "price_band": "Trên 50 triệu"
            }
        ]
    },
    {
        "id": "D11",
        "name": "OPPO A3",
        "brand": "OPPO",
        "storage": "128GB",
        "camera": "50MP",
        "needs": "Cơ bản",
        "battery": "Từ 5000 đến 6000 mAh (Pin sản phẩm 5100 mAh)",
        "charging": "Sạc nhanh (45W)",
        "screen": "Cơ bản (IPS LCD)",
        "chip": "Snapdragon",
        "ram": "8GB",
        "water": "Kháng nhẹ (IP54)",
        "description": "OPPO A3 mang đến một trải nghiệm sử dụng mượt mà và an toàn. Thiết kế bền bỉ theo tiêu chuẩn quân sự và khả năng kháng nước IP54 cho phép thiết bị vượt qua mọi thử thách, từ những buổi dã ngoại đến những cơn mưa bất chợt.",
        "variants": [
            {
                "ram": "8GB",
                "storage": "128GB",
                "price": 5200000,
                "price_band": "5–10 triệu"
            }
        ]
    },
    {
        "id": "D12",
        "name": "OPPO A58",
        "brand": "OPPO",
        "storage": "128GB",
        "camera": "50MP",
        "needs": "Cơ bản",
        "battery": "Từ 4000 đến 5000 mAh (Pin sản phẩm 5000 mAh)",
        "charging": "Sạc nhanh (33W)",
        "screen": "Cơ bản (LTPS LCD)",
        "chip": "Mediatek",
        "ram": "8GB",
        "water": "Kháng nhẹ (IP54)",
        "description": "Thị trường điện thoại di động ngày nay, OPPO A58 là một trong những sản phẩm nổi bật với thiết kế vuông vức và hiện đại. Được thiết kế với mục tiêu tối ưu hóa trải nghiệm người dùng, chiếc điện thoại này mang đến một loạt tính năng ấn tượng trong một thiết kế thon gọn và nhẹ nhàng",
        "variants": [
            {
                "ram": "8GB",
                "storage": "128GB",
                "price": 5400000,
                "price_band": "5–10 triệu"
            }
        ]
    },
    {
        "id": "D13",
        "name": "OPPO A5",
        "brand": "OPPO",
        "storage": "128GB",
        "camera": "50MP",
        "needs": "Cơ bản, Pin khủng",
        "battery": "Từ 5000 đến 6000 mAh (Pin sản phẩm 6000 mAh)",
        "charging": "Sạc nhanh (45W)",
        "screen": "Cơ bản (IPS LCD)",
        "chip": "Snapdragon",
        "ram": "6GB, 8GB",
        "water": "Kháng nhẹ (IP65)",
        "description": "Trong thời đại công nghệ thay đổi nhanh, điện thoại không chỉ để liên lạc hay chạy ứng dụng. Người dùng mong muốn thiết bị đẹp, bền, hỗ trợ sáng tạo và đồng hành lâu dài. OPPO A5 đáp ứng những mong đợi đó với thiết kế lấy cảm hứng từ thiên nhiên, camera AI, pin lớn và độ bền chuẩn quân đội, mang đến trải nghiệm tin cậy mỗi ngày.",
        "variants": [
            {
                "ram": "6GB",
                "storage": "128GB",
                "price": 5290000,
                "price_band": "5–10 triệu"
            },
            {
                "ram": "8GB",
                "storage": "128GB",
                "price": 6290000,
                "price_band": "5–10 triệu"
            }
        ]
    },
    {
        "id": "D14",
        "name": "OPPO A60",
        "brand": "OPPO",
        "storage": "256GB",
        "camera": "50MP",
        "needs": "Cơ bản",
        "battery": "Từ 4000 đến 5000 mAh (Pin sản phẩm 5000 mAh)",
        "charging": "Sạc nhanh (45W)",
        "screen": "Cơ bản (IPS LCD)",
        "chip": "Snapdragon",
        "ram": "8GB",
        "water": "Kháng nhẹ (IP54)",
        "description": "OPPO A60 một sản phẩm mới của OPPO được cho ra mắt tại Việt Nam. Sản phẩm nổi bật từ thiết kế tinh tế đến màn hình sắc nét cùng hàng loạt tính năng nổi bật, thiết bị cam kết mang lại một trải nghiệm độc đáo và khó quên cho người dùng.",
        "variants": [
            {
                "ram": "8GB",
                "storage": "256GB",
                "price": 6380000,
                "price_band": "5–10 triệu"
            }
        ]
    },
    {
        "id": "D15",
        "name": "OPPO A5 Pro",
        "brand": "OPPO",
        "storage": "256GB",
        "camera": "50MP",
        "needs": "Cơ bản",
        "battery": "Từ 5000 đến 6000 mAh (Pin sản phẩm 5800 mAh)",
        "charging": "Sạc nhanh (45W)",
        "screen": "Cơ bản (IPS LCD)",
        "chip": "Snapdragon",
        "ram": "8GB",
        "water": "Kháng cực tốt (IP66, IP68, IP69)",
        "description": "OPPO A5 Pro mang đến trải nghiệm mượt mà với màn hình 90 Hz, hiệu năng vượt trội nhờ Snapdragon và hệ thống camera sắc nét cho từng chi tiết. Cùng với pin 5800 mAh bền bỉ, chiếc điện thoại này sẽ giúp bạn hoàn thành mọi tác vụ và giải trí một cách dễ dàng, không lo gián đoạn.",
        "variants": [
            {
                "ram": "8GB",
                "storage": "256GB",
                "price": 6870000,
                "price_band": "5–10 triệu"
            }
        ]
    },
    {
        "id": "D16",
        "name": "OPPO A5i Pro",
        "brand": "OPPO",
        "storage": "128GB",
        "camera": "50MP",
        "needs": "Cơ bản, Pin khủng",
        "battery": "Từ 5000 đến 6000 mAh (Pin sản phẩm 6000 mAh)",
        "charging": "Sạc nhanh (45W)",
        "screen": "Cơ bản (IPS LCD)",
        "chip": "Snapdragon",
        "ram": "8GB",
        "water": "Kháng nhẹ (IP65)",
        "description": "OPPO A5i Pro là lựa chọn lý tưởng cho ai cần smartphone giá tốt, đáp ứng đủ nhu cầu hàng ngày. Máy nổi bật với chip Snapdragon 6s Gen 1, màn hình lớn mượt mà và pin bền bỉ 6000 mAh. Cùng với camera 50 MP sắc nét và thiết kế tinh tế, OPPO A5i Pro mang đến trải nghiệm trọn vẹn cả công nghệ lẫn thẩm mỹ.",
        "variants": [
            {
                "ram": "8GB",
                "storage": "128GB",
                "price": 5490000,
                "price_band": "5–10 triệu"
            }
        ]
    },
    {
        "id": "D17",
        "name": "OPPO Reno12 F",
        "brand": "OPPO",
        "storage": "256GB",
        "camera": "50MP",
        "needs": "Cơ bản",
        "battery": "Từ 4000 đến 5000 mAh (Pin sản phẩm 5000 mAh)",
        "charging": "Sạc nhanh (45W)",
        "screen": "Màn đẹp (AMOLED)",
        "chip": "Snapdragon",
        "ram": "8GB",
        "water": "Kháng nhẹ (IP64)",
        "description": "OPPO Reno12 F kết hợp hài hòa giữa công nghệ hiện đại và thiết kế tinh tế. Màn hình AMOLED cùng với AI thông minh tạo nên một tổng thể hoàn hảo, đáp ứng mọi nhu cầu của người dùng. Dung lượng pin lớn đảm bảo bạn luôn kết nối với thế giới xung quanh.",
        "variants": [
            {
                "ram": "8GB",
                "storage": "256GB",
                "price": 7160000,
                "price_band": "5–10 triệu"
            }
        ]
    },
    {
        "id": "D18",
        "name": "OPPO Reno12 F 5G",
        "brand": "OPPO",
        "storage": "256GB",
        "camera": "50MP",
        "needs": "Gaming nhẹ",
        "battery": "Từ 4000 đến 5000 mAh (Pin sản phẩm 5000 mAh)",
        "charging": "Sạc nhanh (45W)",
        "screen": "Màn đẹp (AMOLED)",
        "chip": "Mediatek",
        "ram": "12GB",
        "water": "Kháng nhẹ (IP64)",
        "description": "OPPO Reno12 F 5G là chiếc smartphone hiện đại, mang đến sự kết hợp hoàn hảo giữa thiết kế thanh lịch và hiệu năng mạnh mẽ. Với các tính năng tiên tiến và công nghệ sạc nhanh, Reno12 F hứa hẹn mang lại trải nghiệm tuyệt vời cho người dùng trong mọi hoạt động hằng ngày.",
        "variants": [
            {
                "ram": "12GB",
                "storage": "256GB",
                "price": 9810000,
                "price_band": "5–10 triệu"
            }
        ]
    },
    {
        "id": "D19",
        "name": "OPPO A6 Pro 5G",
        "brand": "OPPO",
        "storage": "256GB",
        "camera": "50MP",
        "needs": "Gaming nhẹ, Pin khủng",
        "battery": "Trên 6000 mAh (Pin sản phẩm 6500 mAh)",
        "charging": "Sạc siêu nhanh (80W)",
        "screen": "Màn đẹp (AMOLED)",
        "chip": "Mediatek",
        "ram": "8GB, 12GB",
        "water": "Kháng cực tốt (IP66, IP68, IP69)",
        "description": "OPPO A6 Pro 5G là mẫu smartphone hướng đến người dùng phổ thông cần thiết bị bền bỉ và pin lâu. Máy được thiết kế để hoạt động ổn định trong nhiều điều kiện sử dụng, phù hợp cho nhu cầu liên lạc và giải trí hằng ngày. Sản phẩm nổi bật với viên pin dung lượng lớn, sạc nhanh, màn hình hiển thị tốt và thiết kế được gia cố để tăng khả năng chống chịu.",
        "variants": [
            {
                "ram": "8GB",
                "storage": "256GB",
                "price": 9290000,
                "price_band": "5–10 triệu"
            },
            {
                "ram": "12GB",
                "storage": "256GB",
                "price": 9990000,
                "price_band": "5–10 triệu"
            }
        ]
    },
    {
        "id": "D20",
        "name": "OPPO Reno13 F 5G",
        "brand": "OPPO",
        "storage": "256GB",
        "camera": "50MP",
        "needs": "Gaming nhẹ",
        "battery": "Từ 5000 đến 6000 mAh (Pin sản phẩm 5800 mAh)",
        "charging": "Sạc nhanh (45W)",
        "screen": "Màn đẹp (AMOLED)",
        "chip": "Snapdragon",
        "ram": "8GB",
        "water": "Kháng cực tốt (IP66, IP68, IP69)",
        "description": "OPPO Reno13 F 5G, một thành viên mới toanh của nhà OPPO đã đổ bộ đến Việt Nam. Sở hữu khả năng kháng nước cao, chip Snapdragon mạnh mẽ, dung lượng pin lớn cùng các tính năng AI tiện ích và thiết kế đẹp mắt, tất cả sẽ mang đến cho người dùng yêu thích chụp ảnh hoặc thường xuyên đi du lịch có một người bạn đồng hành đúng điệu.",
        "variants": [
            {
                "ram": "8GB",
                "storage": "256GB",
                "price": 9810000,
                "price_band": "5–10 triệu"
            }
        ]
    },
    {
        "id": "D21",
        "name": "Samsung Galaxy A56 5G",
        "brand": "Samsung",
        "storage": "128GB, 256GB",
        "camera": "50MP",
        "needs": "Gaming tốt, Chụp ảnh – quay phim",
        "battery": "Từ 4000 đến 5000 mAh (Pin sản phẩm 5000 mAh)",
        "charging": "Sạc nhanh (45W)",
        "screen": "Màn đẹp (Super AMOLED)",
        "chip": "Exynos",
        "ram": "8GB, 12GB",
        "water": "Kháng tốt (IP68)",
        "description": "Samsung Galaxy A56 là chiếc điện thoại hiện đại với thiết kế đẹp, bền bỉ và hiệu năng mạnh mẽ. Máy sở hữu camera sắc nét, pin lâu, cùng nhiều tính năng thông minh, giúp bạn làm việc, giải trí và kết nối dễ dàng. Đây là lựa chọn lý tưởng cho những ai cần một chiếc smartphone linh hoạt, đáp ứng tốt mọi nhu cầu hàng ngày.",
        "variants": [
            {
                "ram": "8GB",
                "storage": "128GB",
                "price": 8490000,
                "price_band": "5–10 triệu"
            },
            {
                "ram": "8GB",
                "storage": "256GB",
                "price": 10090000,
                "price_band": "10–15 triệu"
            },
            {
                "ram": "12GB",
                "storage": "256GB",
                "price": 10980000,
                "price_band": "10–15 triệu"
            }
        ]
    },
    {
        "id": "D22",
        "name": "Samsung Galaxy S24",
        "brand": "Samsung",
        "storage": "256GB",
        "camera": "50MP",
        "needs": "Gaming tốt, Chụp ảnh – quay phim",
        "battery": "Từ 4000 đến 5000 mAh (Pin sản phẩm 4000 mAh)",
        "charging": "Sạc nhanh (25W)",
        "screen": "Màn cao cấp (Dynamic AMOLED 2X)",
        "chip": "Exynos",
        "ram": "8GB",
        "water": "Kháng tốt (IP68)",
        "description": "Samsung Galaxy S24. Sản phẩm này mang đến nhiều cải tiến độc đáo, bao gồm việc sử dụng chip mới của Samsung, tích hợp nhiều tính năng thông minh sử dụng trí tuệ nhân tạo và cải thiện đáng kể hiệu suất chụp ảnh từ hệ thống camera",
        "variants": [
            {
                "ram": "8GB",
                "storage": "256GB",
                "price": 16610000,
                "price_band": "15–20 triệu"
            }
        ]
    },
    {
        "id": "D23",
        "name": "Samsung Galaxy S24 FE",
        "brand": "Samsung",
        "storage": "256GB",
        "camera": "50MP",
        "needs": "Gaming tốt, Chụp ảnh – quay phim",
        "battery": "Từ 4000 đến 5000 mAh (Pin sản phẩm 4700 mAh)",
        "charging": "Sạc nhanh (25W)",
        "screen": "Màn cao cấp (Dynamic AMOLED 2X)",
        "chip": "Exynos",
        "ram": "8GB",
        "water": "Kháng tốt (IP68)",
        "description": "Samsung Galaxy S24 FE 256GB mang đến sự nâng cấp vượt trội về hiệu suất và trải nghiệm người dùng. Với vi xử lý Exynos 2400e, máy không chỉ hoạt động mạnh mẽ mà còn tối ưu tốt cho các ứng dụng AI. Bên cạnh đó, màn hình rộng và camera chất lượng cao là những điểm nổi bật khiến Galaxy S24 FE trở nên hấp dẫn.",
        "variants": [
            {
                "ram": "8GB",
                "storage": "256GB",
                "price": 13190000,
                "price_band": "10–15 triệu"
            }
        ]
    },
    {
        "id": "D24",
        "name": "Samsung Galaxy S25 FE",
        "brand": "Samsung",
        "storage": "128GB, 512GB",
        "camera": "50MP",
        "needs": "Gaming tốt, Chụp ảnh – quay phim",
        "battery": "Từ 4000 đến 5000 mAh (Pin sản phẩm 4900 mAh)",
        "charging": "Sạc nhanh (45W)",
        "screen": "Màn cao cấp (Dynamic AMOLED 2X)",
        "chip": "Exynos",
        "ram": "8GB",
        "water": "Kháng tốt (IP68)",
        "description": "Galaxy S25 FE có thiết kế siêu mỏng 7.4 mm và khối lượng 190g, mang lại sự gọn nhẹ hiếm thấy ở dòng FE. Viền màn hình mảnh mở rộng không gian hiển thị, đồng thời giữ cảm giác cầm chắc và thoải mái. Dù màn hình lớn, máy vẫn dễ dùng bằng một tay. Cụm camera đặc trưng của dòng Galaxy tiếp tục được duy trì, tạo vẻ ngoài quen thuộc và tinh tế.",
        "variants": [
            {
                "ram": "8GB",
                "storage": "128GB",
                "price": 13550000,
                "price_band": "10–15 triệu"
            },
            {
                "ram": "8GB",
                "storage": "512GB",
                "price": 16390000,
                "price_band": "15–20 triệu"
            }
        ]
    },
    {
        "id": "D25",
        "name": "Samsung Galaxy S25",
        "brand": "Samsung",
        "storage": "256GB , 512GB",
        "camera": "50 MP",
        "needs": "Cấu hình khủng, Chụp ảnh – quay phim, Mỏng nhẹ",
        "battery": "Từ 4000 đến 5000 mAh (Pin sản phẩm 4000 mAh)",
        "charging": "Sạc nhanh (25W)",
        "screen": "Màn cao cấp (Dynamic AMOLED 2X)",
        "chip": "Snapdragon",
        "ram": "12GB",
        "water": "Kháng tốt (IP68)",
        "description": "Samsung Galaxy S25 - một bước đột phá với thiết kế hiện đại, camera vượt trội và hiệu suất mạnh mẽ. Được trang bị chip Snapdragon 8 Elite For Galaxy tích hợp AI, máy mang đến khả năng tối ưu hóa hiệu năng vượt bậc, đáp ứng mọi nhu cầu của người dùng, đồng thời thể hiện đẳng cấp trong từng chi tiết.",
        "variants": [
            {
                "ram": "12GB",
                "storage": "256GB",
                "price": 22580000,
                "price_band": "20–25 triệu"
            },
            {
                "ram": "12GB",
                "storage": "512GB",
                "price": 24990000,
                "price_band": "20–25 triệu"
            }
        ]
    },
    {
        "id": "D26",
        "name": "Samsung Galaxy S25 Plus",
        "brand": "Samsung",
        "storage": "256GB, 512GB",
        "camera": "50MP",
        "needs": "Cấu hình khủng, Chụp ảnh – quay phim",
        "battery": "Từ 4000 đến 5000 mAh (Pin sản phẩm 4900 mAh)",
        "charging": "Sạc nhanh (45W)",
        "screen": "Màn cao cấp (Dynamic AMOLED 2X)",
        "chip": "Snapdragon",
        "ram": "12GB",
        "water": "Kháng tốt (IP68)",
        "description": "Galaxy S25 Plus không chỉ đáp ứng mọi nhu cầu công việc, giải trí hay sáng tạo mà còn đặt ra chuẩn mực mới cho dòng smartphone cao cấp.",
        "variants": [
            {
                "ram": "12GB",
                "storage": "256GB",
                "price": 26500000,
                "price_band": "25–30 triệu"
            },
            {
                "ram": "12GB",
                "storage": "512GB",
                "price": 29940000,
                "price_band": "25–30 triệu"
            }
        ]
    },
    {
        "id": "D27",
        "name": "Samsung Galaxy Z Flip 7 FE",
        "brand": "Samsung",
        "storage": "128GB, 256GB",
        "camera": "50MP",
        "needs": "Gaming tốt, Chụp ảnh – quay phim",
        "battery": "Từ 4000 đến 5000 mAh (Pin sản phẩm 4000 mAh)",
        "charging": "Sạc nhanh (25W)",
        "screen": "Màn cao cấp (Dynamic AMOLED 2X), Màn hình gập",
        "chip": "Exynos",
        "ram": "8GB",
        "water": "Kháng tốt (IP48)",
        "description": "Samsung Galaxy Z Flip 7 FE không chỉ là một phiên bản mới, mà còn là một tuyên ngôn của Samsung về việc phổ cập hóa công nghệ gập. Mỗi cải tiến trên thiết bị này đều được tính toán kỹ lưỡng để mang lại giá trị thực tiễn cao nhất cho người dùng trong phân khúc \"Fan Edition\".",
        "variants": [
            {
                "ram": "8GB",
                "storage": "128GB",
                "price": 22990000,
                "price_band": "20–25 triệu"
            },
            {
                "ram": "8GB",
                "storage": "256GB",
                "price": 24790000,
                "price_band": "20–25 triệu"
            }
        ]
    },
    {
        "id": "D28",
        "name": "Samsung Galaxy S24 Ultra",
        "brand": "Samsung",
        "storage": "256GB",
        "camera": "200MP",
        "needs": "Gaming tốt, Chụp ảnh – quay phim",
        "battery": "Từ 4000 đến 5000 mAh (Pin sản phẩm 5000 mAh)",
        "charging": "Sạc nhanh (45W)",
        "screen": "Màn cao cấp (Dynamic AMOLED 2X)",
        "chip": "Snapdragon",
        "ram": "12GB",
        "water": "Kháng tốt (IP68)",
        "description": "Samsung Galaxy S24 Ultra mẫu điện thoại cao cấp được ra mắt vào đầu năm 2024, sản phẩm tiếp tục kế thừa và cải tiến từ thế hệ trước. Điểm đặc biệt là sử dụng chip Snapdragon 8 Gen 3 for Galaxy, camera 200 MP và tích hợp nhiều tính năng AI.",
        "variants": [
            {
                "ram": "12GB",
                "storage": "256GB",
                "price": 29450000,
                "price_band": "25–30 triệu"
            }
        ]
    },
    {
        "id": "D29",
        "name": "Samsung Galaxy Z Flip7",
        "brand": "Samsung",
        "storage": "256GB, 512GB",
        "camera": "50MP",
        "needs": "Gaming tốt, Chụp ảnh – quay phim",
        "battery": "Từ 4000 đến 5000 mAh (Pin sản phẩm 4300 mAh)",
        "charging": "Sạc nhanh (25W)",
        "screen": "Màn cao cấp (Dynamic AMOLED 2X), Màn hình gập",
        "chip": "Exynos",
        "ram": "12GB",
        "water": "Kháng tốt (IP48)",
        "description": "Samsung Galaxy Z Flip7, với sự hài hòa giữa thiết kế gập vỏ sò tinh xảo, sức mạnh Galaxy AI tiên phong và độ bền bản lề cải tiến, mang đến trải nghiệm linh hoạt độc bản. Màn hình ngoài Flex Window đa năng, tính năng quay chụp FlexCam rảnh tay và hiệu năng hàng đầu giúp Galaxy Z Flip7 trở thành biểu tượng thời trang lý tưởng để bạn tự do khẳng định chất tôi khác biệt.",
        "variants": [
            {
                "ram": "12GB",
                "storage": "256GB",
                "price": 28990000,
                "price_band": "25–30 triệu"
            },
            {
                "ram": "12GB",
                "storage": "512GB",
                "price": 32990000,
                "price_band": "30–35 triệu"
            }
        ]
    },
    {
        "id": "D30",
        "name": "Samsung Galaxy S25 Ultra",
        "brand": "Samsung",
        "storage": "256GB, 512GB, 1TB",
        "camera": "200MP",
        "needs": "Cấu hình khủng, Chụp ảnh – quay phim",
        "battery": "Từ 4000 đến 5000 mAh ( Pin sản phẩm 5000 mAh)",
        "charging": "Sạc nhanh (45W)",
        "screen": "Màn cao cấp (Dynamic AMOLED 2X)",
        "chip": "Snapdragon",
        "ram": "12GB",
        "water": "Kháng tốt (IP68)",
        "description": "Samsung Galaxy S25 Ultra, với sự kết hợp hoàn hảo giữa thiết kế Titan đẳng cấp, sức mạnh AI tiên phong và hiệu năng không đối thủ, mang đến trải nghiệm quyền năng chưa từng có. Màn hình Dynamic AMOLED 2X sống động, camera 200 MP chuẩn điện ảnh và bút S Pen tích hợp giúp Galaxy S25 Ultra trở thành trợ lý đắc lực, nâng tầm mọi giới hạn sáng tạo và công việc của bạn.",
        "variants": [
            {
                "ram": "12GB",
                "storage": "256GB",
                "price": 33380000,
                "price_band": "30–35 triệu"
            },
            {
                "ram": "12GB",
                "storage": "512GB",
                "price": 36810000,
                "price_band": "35–40 triệu"
            },
            {
                "ram": "12GB",
                "storage": "256GB, 512GB, 1TB",
                "price": 43980000,
                "price_band": "40–45 triệu"
            }
        ]
    },
    {
        "id": "D31",
        "name": "vivo V40 Lite",
        "brand": "Chưa rõ",
        "storage": "256GB",
        "camera": "50MP",
        "needs": "Cơ bản",
        "battery": "Từ 4000 đến 5000 mAh (Pin sản phẩm 5000 mAh)",
        "charging": "Sạc siêu nhanh ( 80W)",
        "screen": "Màn hình đẹp (AMOLED)",
        "chip": "Snapdragon",
        "ram": "8GB",
        "water": "Kháng nhẹ (IP64)",
        "description": "Vivo V40 Lite là chiếc điện thoại mới được thiết kế dành cho những ai yêu thích sự thanh lịch nhưng vẫn đòi hỏi hiệu năng mạnh mẽ và tính năng thông minh. Với khả năng sạc siêu tốc, camera sắc nét và màn hình ấn tượng, sản phẩm hứa hẹn mang đến trải nghiệm công nghệ toàn diện, đáp ứng mọi nhu cầu của người dùng hiện đại.",
        "variants": [
            {
                "ram": "8GB",
                "storage": "256GB",
                "price": 8840000,
                "price_band": "5–10 triệu"
            }
        ]
    },
    {
        "id": "D32",
        "name": "vivo V50 Lite",
        "brand": "Vivo",
        "storage": "256GB",
        "camera": "50MP",
        "needs": "Cơ bản, Pin khủng",
        "battery": "Trên 6000 mAh (Pin sản phẩm 6500 mAh)",
        "charging": "Sạc siêu nhanh (90W)",
        "screen": "Màn hình đẹp (AMOLED)",
        "chip": "Snapdragon",
        "ram": "8GB",
        "water": "Kháng nhẹ (IP65)",
        "description": "Vivo V50 Lite không chỉ thu hút ánh nhìn bởi thiết kế thời thượng mà còn chinh phục người dùng bằng sức mạnh hiệu năng. Với viên pin 6500 mAh, vi xử lý mượt mà, camera đa năng và màn hình sống động, V50 Lite hứa hẹn mang đến trải nghiệm công nghệ toàn diện, đáp ứng mọi nhu cầu cuộc sống hiện đại.",
        "variants": [
            {
                "ram": "8GB",
                "storage": "256GB",
                "price": 8830000,
                "price_band": "5–10 triệu"
            }
        ]
    },
    {
        "id": "D33",
        "name": "vivo V50 Lite 5G",
        "brand": "Vivo",
        "storage": "256GB",
        "camera": "50MP",
        "needs": "Gaming nhẹ, Pin khủng",
        "battery": "Trên 6000 mAh (Pin sản phẩm 6500 mAh)",
        "charging": "Sạc siêu nhanh (90W)",
        "screen": "Màn hình đẹp (AMOLED)",
        "chip": "Mediatek",
        "ram": "8GB, 12GB",
        "water": "Kháng nhẹ (IP65)",
        "description": "Vivo V50 Lite 5G là sự hòa quyện tinh tế giữa vẻ ngoài thanh lịch và sức mạnh hiệu năng bên trong, khi được trang bị viên pin khủng 6500 mAh, CPU MediaTek mạnh mẽ, hệ thống camera sắc nét, màn hình hiển thị ấn tượng,... hứa hẹn mang đến một trải nghiệm công nghệ toàn diện, đáp ứng trọn vẹn mọi yêu cầu của người dùng hiện đại.",
        "variants": [
            {
                "ram": "8GB",
                "storage": "256GB",
                "price": 9810000,
                "price_band": "5–10 triệu"
            },
            {
                "ram": "12GB",
                "storage": "256GB",
                "price": 10800000,
                "price_band": "10–15 triệu"
            }
        ]
    },
    {
        "id": "D34",
        "name": "vivo V30e 5G",
        "brand": "Vivo",
        "storage": "256GB",
        "camera": "50MP",
        "needs": "Gaming nhẹ, Chụp ảnh – quay phim",
        "battery": "Từ 5000 đến 6000 mAh (Pin sản phẩm 5500 mAh)",
        "charging": "Sạch nhanh (44W)",
        "screen": "Màn hình đẹp (AMOLED)",
        "chip": "Snapdragon",
        "ram": "8GB, 12GB",
        "water": "Kháng nhẹ (IP64)",
        "description": "Vivo V30e 5G là điểm nhấn trong thị trường smartphone với sự kết hợp hoàn hảo giữa thiết kế độc đáo, hiệu năng mạnh mẽ và camera chất lượng. Từ màu sắc hấp dẫn, màn hình ấn tượng đến pin bền bỉ, máy đáp ứng đầy đủ nhu cầu của người dùng hiện đại.",
        "variants": [
            {
                "ram": "8GB",
                "storage": "256GB",
                "price": 9320000,
                "price_band": "5–10 triệu"
            },
            {
                "ram": "12GB",
                "storage": "256GB",
                "price": 10300000,
                "price_band": "10–15 triệu"
            }
        ]
    },
    {
        "id": "D35",
        "name": "vivo V60 Lite 5G",
        "brand": "Vivo",
        "storage": "256GB,512GB",
        "camera": "50MP",
        "needs": "Gaming nhẹ, Chụp ảnh – quay phim, Pin khủng",
        "battery": "Trên 6000 mAh (Pin sản phẩm 6500 mAh)",
        "charging": "Sạc siêu nhanh (90W)",
        "screen": "Màn hình đẹp (AMOLED)",
        "chip": "Mediatek",
        "ram": "8GB, 12GB",
        "water": "Kháng nhẹ (IP65)",
        "description": "Vivo V60 Lite 5G là mẫu smartphone tầm trung được thiết kế để đáp ứng tốt nhu cầu sử dụng hằng ngày. Máy trang bị chip MediaTek Dimensity 7360-Turbo, pin 6500 mAh và sạc nhanh 90W, giúp duy trì hoạt động ổn định. Màn hình AMOLED 120 Hz mang lại trải nghiệm xem và thao tác mượt mà. Cấu hình này phù hợp cho người dùng cần thiết bị bền bỉ và giải trí thường xuyên.",
        "variants": [
            {
                "ram": "8GB",
                "storage": "256GB",
                "price": 104900000,
                "price_band": "Trên 50 triệu"
            },
            {
                "ram": "12GB",
                "storage": "512GB",
                "price": 19990000,
                "price_band": "15–20 triệu"
            }
        ]
    },
    {
        "id": "D36",
        "name": "vivo V40 5G",
        "brand": "Vivo",
        "storage": "256GB",
        "camera": "50MP",
        "needs": "Gaming tốt, Chụp ảnh – quay phim",
        "battery": "Từ 5000 đến 6000 mAh (Pin sản phẩm 5500 mAh)",
        "charging": "Sạch siêu nhanh (80W)",
        "screen": "Màn hình đẹp (AMOLED)",
        "chip": "Snapdragon",
        "ram": "12GB",
        "water": "Kháng cực tốt (IP68, IP69)",
        "description": "Vivo V40 5G nổi bật với hệ thống camera chất lượng, cho khả năng chụp ảnh ấn tượng ngay cả trong điều kiện thiếu sáng. Đi kèm với viên pin 5500 mAh bền bỉ, màn hình sắc nét và chip xử lý hiệu quả, máy mang đến một trải nghiệm mượt mà.",
        "variants": [
            {
                "ram": "12GB",
                "storage": "256GB",
                "price": 12760000,
                "price_band": "10–15 triệu"
            }
        ]
    },
    {
        "id": "D37",
        "name": "vivo V60 5G",
        "brand": "Vivo",
        "storage": "256GB, 512GB",
        "camera": "50MP",
        "needs": "Gaming tốt, Chụp ảnh – quay phim, Pin khủng",
        "battery": "Trên 6000 mAh (Pin sản phẩm 6500 mAh)",
        "charging": "Sạch siêu nhanh (90W)",
        "screen": "Màn hình đẹp (AMOLED)",
        "chip": "Snapdragon",
        "ram": "12GB",
        "water": "Kháng cực tốt (IP68, IP69)",
        "description": "Vivo V60 5G là smartphone nổi bật với cụm 4 camera ZEISS sắc nét, màn hình AMOLED 6.77 inch sống động và chip Snapdragon 7 Gen 4 mạnh mẽ. RAM lớn cùng bộ nhớ rộng giúp máy vận hành mượt mà, xử lý đa nhiệm dễ dàng. Đây là lựa chọn hoàn hảo cho người dùng yêu thích công nghệ, sáng tạo hình ảnh và giải trí trọn vẹn.",
        "variants": [
            {
                "ram": "12GB",
                "storage": "256GB",
                "price": 15990000,
                "price_band": "15–20 triệu"
            },
            {
                "ram": "12GB",
                "storage": "512GB",
                "price": 16990000,
                "price_band": "15–20 triệu"
            }
        ]
    },
    {
        "id": "D38",
        "name": "Vivo X300 5G",
        "brand": "Vivo",
        "storage": "256GB",
        "camera": "200MP",
        "needs": "Cấu hình khủng, Chụp ảnh – quay phim, Pin khủng",
        "battery": "Trên 6000 mAh (Pin sản phẩm 6040 mAh)",
        "charging": "Sạc siêu nhanh (90W)",
        "screen": "Màn hình đẹp (AMOLED)",
        "chip": "Mediatek",
        "ram": "12GB",
        "water": "Kháng cực tốt (IP68, IP69)",
        "description": "Vivo X300 5G là mẫu smartphone cao cấp mới của vivo, hướng đến người dùng cần khả năng chụp ảnh tốt, hiệu năng ổn định và trải nghiệm bền bỉ. Máy sở hữu hệ thống camera hợp tác cùng ZEISS, chip Dimensity 9500, màn hình AMOLED sáng cao và pin 6040mAh. Với những nâng cấp thiết thực này, thiết bị đáp ứng tốt nhu cầu chụp ảnh, làm việc và sử dụng lâu dài hằng ngày.",
        "variants": [
            {
                "ram": "12GB",
                "storage": "256GB",
                "price": 23990000,
                "price_band": "20–25 triệu"
            }
        ]
    },
    {
        "id": "D39",
        "name": "Vivo X300 Pro 5G",
        "brand": "Vivo",
        "storage": "512GB",
        "camera": "50MP",
        "needs": "Cấu hình khủng, Chụp ảnh – quay phim, Pin khủng",
        "battery": "Trên 6000 mAh (Pin sản phẩm 6510 mAh)",
        "charging": "Sạc siêu nhanh (90W)",
        "screen": "Màn hình đẹp (AMOLED)",
        "chip": "Mediatek",
        "ram": "16GB",
        "water": "Kháng cực tốt (IP68, IP69)",
        "description": "Vivo X300 Pro 5G là flagship hướng đến nhiếp ảnh, hiệu năng và độ bền dài hạn. Máy nổi bật với hệ thống camera ZEISS, chip Dimensity 9500, màn hình LTPO 120 Hz và pin BlueVolt dung lượng lớn, đáp ứng tốt nhu cầu chụp ảnh, giải trí và làm việc. Dựa trên thông số chi tiết, X300 Pro cho thấy định hướng tối ưu trải nghiệm trong phân khúc cao cấp.",
        "variants": [
            {
                "ram": "16GB",
                "storage": "512GB",
                "price": 34990000,
                "price_band": "30–35 triệu"
            }
        ]
    }
]

PRICE_BANDS = [
    "Dưới 5 triệu", "5–10 triệu", "10–15 triệu", "15–20 triệu",
    "20–25 triệu", "25–30 triệu", "30–35 triệu", "35–40 triệu",
    "40–45 triệu", "45–50 triệu", "Trên 50 triệu"
]

def money(value):
    return f"{value:,.0f}".replace(",", ".") + "đ"

def battery_group(value):
    """Chuẩn hóa nhóm pin dựa trên thông tin trong báo cáo."""
    s = value.lower()
    if "dưới 4000" in s:
        return "Dưới 4000 mAh"
    if "4000 đến 5000" in s or "4000-5000" in s:
        return "4000–5000 mAh"
    if "5000 đến 6000" in s or "5000-6000" in s:
        return "5000–6000 mAh"
    if "trên 6000" in s:
        return "Trên 6000 mAh"
    return "Chưa rõ"

def charging_group(value):
    s = value.lower()
    if "siêu nhanh" in s:
        return "Sạc siêu nhanh"
    if "nhanh" in s:
        return "Sạc nhanh"
    return "Khác / chưa rõ"

def screen_group(value):
    s = value.lower()
    if "amoled" in s or "oled" in s:
        return "Màn hình đẹp (OLED/AMOLED)"
    return "Màn hình cơ bản"

def all_needs():
    result = set()
    for p in PHONES:
        for need in p["needs"].split(","):
            need = need.strip()
            if need:
                result.add(need)
    return sorted(result, key=str.casefold)

def infer_phones(brand, budget, need, battery, charging, screen, ram, storage):
    """Máy suy diễn: lọc các sự kiện theo tiêu chí người dùng và trả về luật khớp."""
    results = []
    for p in PHONES:
        if brand != "Tất cả" and p["brand"].casefold() != brand.casefold():
            continue
        if need != "Tất cả" and need.casefold() not in p["needs"].casefold():
            continue
        if battery != "Tất cả" and battery_group(p["battery"]) != battery:
            continue
        if charging != "Tất cả" and charging_group(p["charging"]) != charging:
            continue
        if screen != "Tất cả" and screen_group(p["screen"]) != screen:
            continue

        variants = []
        for v in p["variants"]:
            if budget != "Tất cả" and v["price_band"] != budget:
                continue
            if ram != "Tất cả" and v["ram"] != ram:
                continue
            # Một số dòng dữ liệu ghi nhiều mức dung lượng trong cùng một chuỗi.
            # Tách các mức này để bộ lọc hoạt động theo từng dung lượng riêng.
            variant_storages = [item.strip() for item in v["storage"].split(",")]
            if storage != "Tất cả" and storage not in variant_storages:
                continue
            # Khi người dùng chọn một dung lượng cụ thể, chỉ hiển thị đúng dung lượng đó,
            # không hiện lại chuỗi gộp như "256GB, 512GB, 1TB".
            if storage != "Tất cả":
                matched_variant = dict(v)
                matched_variant["storage"] = storage
                variants.append(matched_variant)
            else:
                variants.append(v)
        if not variants:
            continue

        # Luật giải thích được sinh từ các tiêu chí đã chọn và thông tin điện thoại.
        conditions = [
            f"Hãng={p['brand']}",
            f"Nhu cầu={need if need != 'Tất cả' else p['needs']}",
            f"Pin={battery if battery != 'Tất cả' else battery_group(p['battery'])}",
            f"Sạc={charging if charging != 'Tất cả' else charging_group(p['charging'])}",
            f"Màn hình={screen if screen != 'Tất cả' else screen_group(p['screen'])}",
        ]
        results.append({"phone": p, "variants": variants,
                        "rule": " ∧ ".join(conditions) + f" → {p['id']}"})

    return results

st.title("📱 HỆ CHUYÊN GIA TƯ VẤN LỰA CHỌN MUA ĐIỆN THOẠI")
st.caption("Đề tài Nhập môn Trí tuệ nhân tạo | Python + Streamlit")
st.write(
    "Chọn các tiêu chí mong muốn. Hệ thống sẽ đối chiếu với cơ sở tri thức "
    "được tổng hợp từ báo cáo, sau đó hiển thị điện thoại và các cấu hình phù hợp."
)

def reset_phone_filters():
    """Khi đổi hãng, xóa các lựa chọn cũ để bộ lọc được tính lại theo hãng mới."""
    for key in ("selected_budget", "selected_need", "selected_battery", "selected_charging", "selected_screen", "selected_ram", "selected_storage"):
        st.session_state[key] = "Tất cả"


def _matches_phone_and_variant(phone, variant, omit=None):
    """Kiểm tra các tiêu chí hiện tại, bỏ qua một tiêu chí để tạo danh sách lựa chọn hợp lệ."""
    values = {
        "brand": st.session_state.get("selected_brand", "Tất cả"),
        "budget": st.session_state.get("selected_budget", "Tất cả"),
        "need": st.session_state.get("selected_need", "Tất cả"),
        "battery": st.session_state.get("selected_battery", "Tất cả"),
        "charging": st.session_state.get("selected_charging", "Tất cả"),
        "screen": st.session_state.get("selected_screen", "Tất cả"),
        "ram": st.session_state.get("selected_ram", "Tất cả"),
        "storage": st.session_state.get("selected_storage", "Tất cả"),
    }
    if omit != "brand" and values["brand"] != "Tất cả" and phone["brand"].casefold() != values["brand"].casefold():
        return False
    if omit != "need" and values["need"] != "Tất cả" and values["need"].casefold() not in phone["needs"].casefold():
        return False
    if omit != "battery" and values["battery"] != "Tất cả" and battery_group(phone["battery"]) != values["battery"]:
        return False
    if omit != "charging" and values["charging"] != "Tất cả" and charging_group(phone["charging"]) != values["charging"]:
        return False
    if omit != "screen" and values["screen"] != "Tất cả" and screen_group(phone["screen"]) != values["screen"]:
        return False
    if omit != "budget" and values["budget"] != "Tất cả" and variant["price_band"] != values["budget"]:
        return False
    if omit != "ram" and values["ram"] != "Tất cả" and variant["ram"] != values["ram"]:
        return False
    variant_storages = [x.strip() for x in variant["storage"].split(",")]
    if omit != "storage" and values["storage"] != "Tất cả" and values["storage"] not in variant_storages:
        return False
    return True


def available_values(field):
    """Sinh lựa chọn từ các sản phẩm còn phù hợp với những tiêu chí khác đang chọn."""
    values = set()
    for phone in PHONES:
        for variant in phone["variants"]:
            if not _matches_phone_and_variant(phone, variant, omit=field):
                continue
            if field == "brand":
                values.add(phone["brand"])
            elif field == "budget":
                values.add(variant["price_band"])
            elif field == "need":
                values.update(x.strip() for x in phone["needs"].split(",") if x.strip())
            elif field == "battery":
                values.add(battery_group(phone["battery"]))
            elif field == "charging":
                values.add(charging_group(phone["charging"]))
            elif field == "screen":
                values.add(screen_group(phone["screen"]))
            elif field == "ram":
                values.add(variant["ram"])
            elif field == "storage":
                values.update(x.strip() for x in variant["storage"].split(",") if x.strip())

    values = {v for v in values if v}
    if field == "budget":
        return sorted(values, key=lambda x: PRICE_BANDS.index(x) if x in PRICE_BANDS else len(PRICE_BANDS))
    if field == "ram":
        return sorted(values, key=lambda x: int(x.replace("GB", "")) if x.replace("GB", "").isdigit() else 9999)
    if field == "storage":
        def _storage_key(value):
            value = value.upper().strip()
            if value.endswith("TB"):
                return int(value[:-2]) * 1024
            if value.endswith("GB"):
                return int(value[:-2])
            return 999999
        return sorted(values, key=_storage_key)
    if field == "battery":
        order = ["Dưới 4000 mAh", "4000–5000 mAh", "5000–6000 mAh", "Trên 6000 mAh", "Chưa rõ"]
        return sorted(values, key=lambda x: order.index(x) if x in order else len(order))
    return sorted(values, key=str.casefold)


with st.container(border=True):
    st.subheader("Thông tin tư vấn")
    c1, c2, c3 = st.columns(3)
    all_brands = sorted({p["brand"] for p in PHONES}, key=str.casefold)
    selected_brand = st.selectbox(
        "Hãng sản xuất", ["Tất cả"] + all_brands,
        key="selected_brand", on_change=reset_phone_filters
    )

    # Mỗi danh sách được tính từ dữ liệu sản phẩm còn phù hợp với các tiêu chí khác.
    # Nếu lựa chọn cũ không còn hợp lệ sau khi đổi tiêu chí, tự đặt lại về "Tất cả".
    filter_specs = [
        ("selected_budget", "budget", "Khoảng giá"),
        ("selected_need", "need", "Mục đích sử dụng"),
        ("selected_battery", "battery", "Dung lượng pin"),
        ("selected_charging", "charging", "Công nghệ sạc"),
        ("selected_screen", "screen", "Màn hình"),
        ("selected_ram", "ram", "RAM"),
        ("selected_storage", "storage", "Bộ nhớ trong"),
    ]
    option_map = {}
    for key, field, _label in filter_specs:
        vals = ["Tất cả"] + available_values(field)
        if st.session_state.get(key, "Tất cả") not in vals:
            st.session_state[key] = "Tất cả"
        option_map[key] = vals

    with c1:
        selected_budget = st.selectbox("Khoảng giá", option_map["selected_budget"], key="selected_budget")
        selected_need = st.selectbox("Mục đích sử dụng", option_map["selected_need"], key="selected_need")
    with c2:
        selected_battery = st.selectbox("Dung lượng pin", option_map["selected_battery"], key="selected_battery")
        selected_charging = st.selectbox("Công nghệ sạc", option_map["selected_charging"], key="selected_charging")
        selected_screen = st.selectbox("Màn hình", option_map["selected_screen"], key="selected_screen")
    with c3:
        selected_ram = st.selectbox("RAM", option_map["selected_ram"], key="selected_ram")
        selected_storage = st.selectbox("Bộ nhớ trong", option_map["selected_storage"], key="selected_storage")
        st.caption("Các lựa chọn tự cập nhật theo dữ liệu điện thoại còn phù hợp với những tiêu chí khác bạn đã chọn.")
    search_clicked = st.button("🔎 Tư vấn điện thoại", type="primary", use_container_width=True)

if search_clicked:
    st.session_state["phone_results"] = infer_phones(
        selected_brand, selected_budget, selected_need, selected_battery,
        selected_charging, selected_screen, selected_ram, selected_storage
    )
    st.session_state["phone_criteria"] = {
        "brand": selected_brand, "budget": selected_budget, "need": selected_need,
        "battery": selected_battery, "charging": selected_charging,
        "screen": selected_screen, "ram": selected_ram, "storage": selected_storage
    }

if "phone_results" in st.session_state:
    results = st.session_state["phone_results"]
    st.divider()
    st.subheader(f"Kết quả tư vấn: {len(results)} điện thoại phù hợp")
    if not results:
        st.warning("Chưa có dữ liệu sản phẩm để hiển thị.")
    else:
        st.info("Chỉ hiển thị điện thoại và cấu hình có thật trong dữ liệu, khớp với các tiêu chí bạn đã chọn. Nếu không có sản phẩm phù hợp, hãy đổi hoặc bỏ bớt một tiêu chí.")
        for item in results:
            p = item["phone"]
            with st.container(border=True):
                st.markdown(f"### 📱 {p['name']}  ·  {p['id']}")
                image_col, info_col = st.columns([1, 2])
                with image_col:
                    image_path = get_phone_image(p["id"])
                    if image_path:
                        st.image(image_path, use_container_width=True)
                    else:
                        st.caption("Chưa có ảnh. Thêm ảnh vào thư mục images với tên như D1.jpg.")
                with info_col:
                    st.write(p["description"])
                left, right = st.columns(2)
                with left:
                    st.write(f"**Hãng:** {p['brand']}")
                    st.write(f"**Nhu cầu:** {p['needs']}")
                    st.write(f"**Camera:** {p['camera']}")
                    st.write(f"**Pin:** {p['battery']}")
                    st.write(f"**Sạc:** {p['charging']}")
                    st.write(f"**Màn hình:** {p['screen']}")
                with right:
                    st.write(f"**Chip:** {p['chip']}")
                    st.write(f"**RAM theo báo cáo:** {p['ram']}")
                    st.write(f"**Bộ nhớ theo báo cáo:** {p['storage']}")
                    st.write(f"**Kháng nước, bụi:** {p['water']}")
                    st.markdown("**Cấu hình và giá khớp tiêu chí:**")
                    for v in item["variants"]:
                        st.write(f"- RAM {v['ram']} · {v['storage']} · **{money(v['price'])}** ({v['price_band']})")
                with st.expander("Xem luật suy diễn"):
                    st.code(item["rule"], language="text")

st.divider()
st.caption(
    "Lưu ý: Đây là hệ thống hỗ trợ ra quyết định dựa trên dữ liệu của bài tập lớn, "
    "không thay thế việc kiểm tra thông số và giá bán thực tế tại cửa hàng."
)
