---
tags: [Data Center, Trung tâm dữ liệu, Space, Không gian, Environment, Môi trường, Infrastructure, Hạ tầng, AI, Technology]
---

# Tranh cãi về trung tâm dữ liệu ngoài không gian

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120304.webp)

Cầu Menhu trên Đại Vận Hà Hàng Châu là một cây cầu đi bộ nằm tại nơi giao nhau giữa Đại Vận Hà và sông Tiền Đường, sắp sửa khánh thành. Thiết kế ba nhịp vòm của nó tượng trưng cho nghệ thuật thêu Hàng Châu và những con sóng trên sông Tiền Đường. ([via](https://www.163.com/dy/article/KDAJVKT50514ETGI.html))

## Tranh cãi về trung tâm dữ liệu ngoài không gian

Sự bùng nổ của AI khiến các trung tâm dữ liệu không còn đủ chỗ. Chi phí xây dựng và vận hành đang tăng vọt.

Nhiều người bắt đầu đưa ra ý tưởng đưa trung tâm dữ liệu lên không gian.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025113006.webp)

Đầu tiên là [Elon Musk nói](https://news.cctv.com/2025/11/11/ARTI6f0b2Jz9Q1WnTzbvH00W251111.shtml) rằng SpaceX đang cân nhắc xây dựng trung tâm dữ liệu trên quỹ đạo Trái Đất.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025113007.webp)

Sau đó, trong tuần này, Ủy ban Khoa học và Công nghệ Thành phố Bắc Kinh cùng Ban Quản lý Công viên Khoa học Trung Quan Thôn đã công bố [“Phương án Quy hoạch Xây dựng Trung tâm Dữ liệu Không gian”](https://finance.sina.com.cn/tech/roll/2025-11-28/doc-infywkcw9025829.shtml).

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025113008.webp)

Mục tiêu là “xây dựng cụm trung tâm dữ liệu với hàng triệu card trên quỹ đạo cách mặt đất 700 km, thực hiện các dịch vụ truyền dẫn và tính toán dữ liệu từ không gian”.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025113009.webp)

Theo các báo cáo, giới chuyên gia cho rằng việc đưa trung tâm dữ liệu lên không gian là “[xu thế tất yếu](https://finance.sina.cn/7x24/2025-11-29/detail-infyzkhk9168276.d.html)” (hình trên).

> (1) Trung tâm dữ liệu trên quỹ đạo cao có thể tận dụng năng lượng mặt trời cường độ mạnh 24/7. Vì không bị khí quyển ảnh hưởng, hiệu suất phát điện có thể đạt tới 95%.
> 
> (2) Nhiệt độ ngoài không gian sâu khoảng -270 độ. Chỉ cần lắp đặt vật liệu dẫn nhiệt là có thể tản nhiệt, không cần hệ thống làm mát bằng chất lỏng phức tạp, giúp tiết kiệm chi phí đáng kể.

Tôi thấy đây là hai lợi thế rất lớn. Trung tâm dữ liệu không gian thực sự nên được triển khai sớm.

Tuy nhiên, ngay sau đó tôi lại đọc được [một bài viết khác](https://taranis.ie/datacenters-in-space-are-a-terrible-horrible-no-good-idea/).

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025113010.webp)

Tác giả là một kỹ sư kỳ cựu tại NASA, từng tham gia thiết kế vệ tinh.

Dựa trên kinh nghiệm từ Trạm Vũ trụ Quốc tế (ISS), ông cho rằng rào cản công nghệ hiện nay là quá lớn. Trung tâm dữ liệu không gian rất khó thực thi. Nếu cố làm, chi phí sẽ cực lớn mà lợi ích thu về chẳng bao nhiêu.

Đây là lần đầu tiên tôi thấy có người phản biện vấn đề này một cách nghiêm túc. Tôi không có chuyên môn trong lĩnh vực này nên không rõ các phép tính của ông ấy có chính xác không. Hơn nữa, ISS đã hoàn thành từ 25 năm trước, công nghệ bây giờ chắc chắn đã vượt xa thời đó.

Tôi xin chia sẻ vài điểm nghi vấn của ông ấy để mọi người cùng xem liệu trung tâm dữ liệu không gian có thực sự triển vọng.

**1. Vấn đề năng lượng**

Năng lượng trong không gian chủ yếu đến từ mặt trời. Tấm pin mặt trời lớn nhất hiện nay nằm trên ISS với công suất đỉnh hơn 200kW. Tuy nhiên, diện tích của nó cực lớn, khoảng 2500 mét vuông, rộng hơn nửa sân bóng đá Mỹ.

Một chiếc card Nvidia H200 tiêu thụ khoảng 0,7kW, thực tế vận hành có thể cần tới 1kW nguồn điện. Tấm pin của ISS chỉ đủ cấp điện cho khoảng 200 chiếc H200.

Để so sánh, trung tâm dữ liệu mà OpenAI sắp xây dựng tại Na Uy dự kiến chứa 100.000 GPU, mỗi chiếc có công suất còn cao hơn cả H200.

**2. Vấn đề tản nhiệt**

Không gian rất lạnh, gần độ không tuyệt đối. Thoạt nhìn việc tản nhiệt có vẻ dễ dàng. Nhưng thực tế chỉ có hai cách tản nhiệt: qua môi trường dẫn hoặc qua bức xạ.

Không gian gần như chân không, không có không khí nên không thể dùng đối lưu không khí để tản nhiệt. Các tấm tản nhiệt và quạt trên GPU hoàn toàn vô dụng.

Cách duy nhất là dùng làm mát bằng chất lỏng để dẫn nhiệt ra các tấm tản nhiệt lớn, sau đó bức xạ nhiệt vào không gian (các tấm này phải đặt ở mặt khuất mặt trời).

ISS đang dùng hệ thống bức xạ nhiệt. Hệ thống này rất phức tạp nhưng giới hạn tản nhiệt chỉ là 16kW, tương đương với 16 chiếc H200. Con số này chỉ bằng hơn một phần tư so với một tủ rack máy chủ thông thường dưới mặt đất.

Tấm tản nhiệt của ISS có kích thước 13,6m x 3,12m, tức khoảng 42,5 mét vuông. Để tản nhiệt cho 200 chiếc H200, diện tích cần tăng gấp 12,5 lần, lên khoảng 531 mét vuông. Diện tích này gấp 2,6 lần so với tấm pin mặt trời cùng công suất.

Như vậy, trung tâm dữ liệu không gian sẽ trở nên khổng lồ, vượt xa ISS, trong khi năng lực tính toán chỉ bằng ba tủ rack tiêu chuẩn dưới mặt đất.

**3. Vấn đề tia hạt năng lượng cao**

Không gian đầy rẫy các hạt tốc độ cao. Vì không có khí quyển bảo vệ, chúng có thể va đập trực tiếp và làm hỏng vật liệu chip. Phổ biến nhất là lỗi SEU (Single Event Upset), khi một hạt va chạm làm đảo ngược một bit dữ liệu.

Trung tâm dữ liệu không gian phải hoạt động lâu dài nên còn chịu hiệu ứng tổng liều bức xạ. Việc va chạm liên tục khiến tốc độ đóng ngắt của bóng bán dẫn chậm đi và cuối cùng ngừng hoạt động.

Chúng ta cần lớp bảo vệ, nhưng những tia vũ trụ mạnh nhất có thể xuyên qua lớp chì dày kinh khủng. Trong khi đó, khả năng vận chuyển của tàu vũ trụ có hạn, không thể mang theo lớp bảo vệ quá dày.

Để tăng khả năng kháng bức xạ cho GPU và bộ nhớ, chúng ta buộc phải thiết kế lại chip cho môi trường không gian. Nhưng những con chip như vậy sẽ có hiệu năng kém xa GPU dưới mặt đất.

**4. Vấn đề truyền thông**

Hầu hết vệ tinh liên lạc với mặt đất qua sóng vô tuyến. Việc đạt tốc độ trên 1Gbps là rất khó khăn. Dù có các giải pháp laser giúp tăng băng thông, nhưng chúng lại đòi hỏi điều kiện khí quyển lý tưởng.

Ngược lại, các trung tâm dữ liệu dưới mặt đất có thể kết nối với nhau với tốc độ tối thiểu 100Gbps.

## [Phần mềm tuần này] Dịch vụ kết nối mô hình lớn của Qiniu Cloud

Cách đây vài tuần, tôi đã [giới thiệu](https://www.ruanyifeng.com/blog/2025/10/weekly-issue-370.html) [Qiniu Cloud](https://s.qiniu.com/JrUbmm), một nền tảng cho phép gọi mọi mô hình AI lớn trong và ngoài nước, có thể coi là OpenRouter của Trung Quốc.

Tuy nhiên, tôi chưa nói rõ hai điểm khiến nhiều bạn gặp rắc rối.

Thứ Hai tuần này, DeepSeek vừa ra mắt phiên bản V3.2 Speciale và bản thường, tối cùng ngày Qiniu Cloud đã cập nhật ngay (hình dưới). Họ cập nhật nhanh như vậy nên tôi muốn bổ sung thêm vài thông tin để các bạn không gặp lỗi nữa.

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120202.webp)

**1. Các mô hình nước ngoài.** Qiniu Cloud hiện cung cấp hơn 70 mô hình, nhưng vì nhiều lý do, các mô hình nước ngoài không xuất hiện trên trang chủ dù thực tế vẫn được hỗ trợ.

Bạn có thể tra cứu danh sách mô hình cụ thể tại [website này](https://sufy.com/zh-CN/services/ai-inference/models), hầu hết các mô hình phổ biến đều có (hình dưới).

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120201.webp)

Sau khi tìm được Model ID (ví dụ `claude-4.5-opus`), bạn chỉ cần dùng ID đó làm tham số tên mô hình là có thể gọi được trên Qiniu Cloud.

**2. Tần suất yêu cầu.** Với nhà phát triển thông thường, mức “5 lần/phút, 60 lần/giờ” là đủ dùng. Nếu vượt quá tốc độ này, bạn sẽ gặp lỗi (mã trạng thái 429).

Đừng thấy giới hạn này quá ngặt nghèo. Để so sánh, gói Pro chính thức của Claude cũng chỉ cho phép 45 lần trong 5 giờ.

Tôi giới thiệu Qiniu Cloud vì đây là công ty đã niêm yết, dịch vụ có bảo đảm. Ngoài ra, họ hỗ trợ cả định dạng gọi của OpenAI và Anthropic, rất tiện lợi khi dùng API (hình dưới).

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120203.webp)

**Người dùng mới sẽ được tặng miễn phí 3 triệu Token**. Nếu mời thêm một người bạn, bạn sẽ có thêm 5 triệu Token và người bạn đó nhận được 10 triệu Token. Lưu ý, số Token miễn phí này có thể dùng cho bất kỳ mô hình nào họ cung cấp. Mời bạn sử dụng [link giới thiệu](https://s.qiniu.com/JrUbmm) của tôi để đăng ký.

## Tin tức công nghệ

1、[Khủng hoảng dòng hải lưu tại Iceland](https://www.dagens.com/news/iceland-declares-ocean-current-instability-a-national-security-risk)

Chính phủ Iceland tuyên bố sự thay đổi các dòng hải lưu ở Đại Tây Dương là vấn đề an ninh quốc gia, đe dọa sự sinh tồn của đất nước.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025113005.webp)

Dữ liệu quan sát cho thấy vòng hoàn lưu Đại Tây Dương đang suy yếu do nóng lên toàn cầu. Vòng hoàn lưu này đóng vai trò như một băng tải khổng lồ đưa nước ấm từ xích đạo lên phía Bắc, tạo ra khí hậu ấm áp cho vùng Bắc Đại Tây Dương.

Nếu dòng hải lưu này biến mất, nhiệt độ tại Iceland sẽ giảm mạnh. Trong kịch bản tồi tệ nhất, đảo quốc này có thể bị băng hà bao phủ, thực sự trở thành một “hòn đảo băng” và không còn người ở được nữa.

2、[Âm thanh trên sao Hỏa](https://gizmodo.com/weve-detected-lightning-on-mars-for-the-first-time-2000691996)

Trên sao Hỏa có những âm thanh gì?

Các nhà khoa học cũng rất muốn biết. Robot tự hành Perseverance của Mỹ khi đổ bộ lên sao Hỏa vào tháng 2 năm 2021 đã được trang bị một microphone chuyên dụng để lắng nghe âm thanh nơi đây.

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120104.webp)

Hình trên là microphone gắn cùng camera ở đỉnh robot.

Gần đây, một nhóm nghiên cứu đã phân tích 28 giờ âm thanh thu được.

Họ nghe thấy tiếng vật thể va chạm vào bề mặt, đồng thời quan sát thấy tín hiệu điện. Từ đó, họ suy đoán đây là tiếng sấm sét.

Đây là lần đầu tiên chúng ta biết sao Hỏa có sét. Vì không khí ở đó rất mỏng, không có nước nên không có mây, đồng nghĩa không có hiện tượng phóng điện giữa các đám mây. Các nhà khoa học nhận định sét trên sao Hỏa có thể do ma sát của cát đá trong các cơn lốc xoáy tạo ra.

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120105.webp)

3、[Lá cây nhân tạo](https://newscenter.lbl.gov/2025/04/24/scientists-develop-artificial-leaf-that-uses-sunlight-to-produce-valuable-chemicals/)

Một nhóm nghiên cứu Mỹ đã chế tạo các tấm pin mặt trời dưới hình dạng những chiếc lá.

![](https://cdn.beekka.com/blogimg/asset/202504/bg2025042813.webp)

Phần dưới của những chiếc lá này kết nối với các chất xúc tác hóa học. Nhờ năng lượng mặt trời, chúng có thể chuyển hóa CO2 và nước thành nhiên liệu.

Nếu lắp ghép nhiều chiếc lá như vậy thành một cái cây, chúng ta sẽ có một thiết bị sản xuất nhiên liệu.

![](https://cdn.beekka.com/blogimg/asset/202504/bg2025042814.webp)

Điều này gợi ý rằng thiết bị năng lượng mặt trời không nhất thiết phải là những tấm phẳng khô khan, chúng hoàn toàn có thể mang hình dáng của cây xanh.

## Bài viết

1、[Giải trình về báo cáo bảo mật gần đây](https://mp.weixin.qq.com/s/E8YQLWZFM2J7r5DZNSl47w) (tiếng Trung)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120403.webp)

Một đội ngũ bảo mật nước ngoài gần đây [báo cáo](https://programnotes.cn/browser-security-ShadyPanda/index.html) rằng một số tiện ích trình duyệt (như Clean Master, WeTab) là mã độc. Đây là phản hồi từ đội ngũ phát triển Trung Quốc của các tiện ích này.

Họ cho biết Clean Master đã được bán từ năm ngoái và hiện không còn liên quan đến họ. Còn các tiện ích khác bị nhận diện nhầm. Lời khuyên là hãy đọc kỹ [báo cáo bảo mật](https://programnotes.cn/browser-security-ShadyPanda/index.html) trước khi xem bài phản hồi này. ([@yiGmMk](https://github.com/ruanyf/weekly/issues/8349) đóng góp)

2、[Electron đối đầu Tauri](https://www.dolthub.com/blog/2025-11-13-electron-vs-tauri/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112801.webp)

Electron và Tauri hiện là hai giải pháp chính để phát triển ứng dụng máy tính đa nền tảng. Bài viết này so sánh chi tiết ưu và nhược điểm của từng loại.

3、[Tại sao tôi chuyển đi khỏi GitHub](https://dillo-browser.org/news/migration-from-github/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120103.webp)

Tác giả cảm thấy GitHub không còn phù hợp vì quá nặng nề, nên đã tự xây dựng giải pháp lưu trữ mã nguồn riêng. Nếu bạn cũng muốn tự dựng máy chủ quản lý mã nguồn, đây là một tài liệu tham khảo tốt.

4、[Protobuf tốt hơn JSON](https://aloisdeniel.com/blog/better-than-json) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120215.webp)

Bài viết kêu gọi sử dụng định dạng Protobuf thay thế cho JSON. Tác giả cho rằng ưu điểm duy nhất của JSON là con người có thể đọc được.

5、[Cách viết file CLAUDE.md hiệu quả](https://www.humanlayer.dev/blog/writing-a-good-claude-md) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120102.webp)

Nhiều công cụ lập trình AI sử dụng một file văn bản làm ngữ cảnh cho mỗi lần yêu cầu. Bài viết này lấy ví dụ về CLAUDE.md để hướng dẫn cách tận dụng tốt file này.

6、[Hệ thống file ZFS vượt trội hơn Btrfs](https://www.xda-developers.com/how-zfs-is-superior-to-btrfs/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202502/bg2025022202.webp)

ZFS và Btrfs là hai hệ thống file hiện đại phổ biến. Bài viết giới thiệu đặc điểm của chúng và lập luận rằng ZFS đáng tin cậy hơn.

## Công cụ

1、[Fizzy](https://github.com/basecamp/fizzy)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120401.webp)

Công ty 37Signals vừa mã nguồn mở ứng dụng Kanban mà họ sử dụng nội bộ.

2、[Fresh](https://github.com/sinelaw/fresh)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120402.webp)

Một trình soạn thảo văn bản chạy trên terminal.

3、[Gitmal](https://github.com/antonmedv/gitmal)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120216.webp)

Công cụ này biến kho lưu trữ Git thành một website tĩnh, nội dung web bao gồm các file, các bản commit và làm nổi bật mã nguồn.

4、[GitHub Card](https://githubcard.com)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112802.webp)

Website giúp tạo các thẻ chia sẻ cho người dùng và kho lưu trữ GitHub. ([@Cactusinhand](https://github.com/ruanyf/weekly/issues/8303) đóng góp)

5、[EasyDB](https://github.com/shencangsheng/easydb_app)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112804.webp)

Ứng dụng máy tính đa nền tảng, dùng SQL để truy vấn các tệp dữ liệu như database, CSV, Excel, JSON. ([@shencangsheng](https://github.com/ruanyf/weekly/issues/8313) đóng góp)

6、[Webhooker](https://github.com/TokenRollAI/webhooker)

Một cổng chuyển tiếp Webhook, ví dụ như chuyển tin nhắn từ Slack sang Lark hoặc DingTalk. ([@Disdjj](https://github.com/ruanyf/weekly/issues/8318) đóng góp)

7、[PySInfo](https://github.com/EasyCam/Pysinfo)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120101.webp)

Một kịch bản Python dùng để hiển thị thông tin hệ thống trên dòng lệnh, tương tự như [fastfetch](https://github.com/fastfetch-cli/fastfetch). ([@cycleuser](https://github.com/ruanyf/weekly/issues/8333) đóng góp)

8、[PocketMocker](https://github.com/tianchangNorth/pocket-mocker)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120204.webp)

Thư viện Mock cho frontend web, hoạt động bằng cách chặn fetch và XMLHttpRequest ngay trong trình duyệt, có kèm bảng điều khiển trực quan. ([@tianchangNorth](https://github.com/ruanyf/weekly/issues/8345) đóng góp)

9、[code996](https://github.com/hellodigua/code996)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120302.webp)

Công cụ dòng lệnh giúp phân tích thời gian commit trên Git để đánh giá cường độ làm việc và tình trạng làm thêm giờ của dự án. ([@hellodigua](https://github.com/ruanyf/weekly/issues/8361) đóng góp)

10、[Ngọc Đào Văn Hưởng Hiên](https://github.com/nicejade/markdown2png)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120305.webp)

Ứng dụng web mã nguồn mở giúp chuyển văn bản Markdown thành hình ảnh. ([@nicejade](https://github.com/ruanyf/weekly/issues/8363) đóng góp)

## Liên quan đến AI

1、[ClipSketch AI](https://github.com/RanFeng/clipsketch-ai)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120217.webp)

Ứng dụng web mã nguồn mở sử dụng mô hình Gemini để chuyển các video từ Xiaohongshu và Bilibili thành các câu chuyện vẽ tay. ([@RanFeng](https://github.com/ruanyf/weekly/issues/8353) đóng góp)

2、[Banana Prompt Quicker](https://github.com/glidea/banana-prompt-quicker)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120306.webp)

Tiện ích trình duyệt mã nguồn mở tổng hợp các prompt phổ biến cho mô hình Nano Banana, giúp người dùng dễ dàng sử dụng lại. ([@glidea](https://github.com/ruanyf/weekly/issues/8364) đóng góp)

3、[git-rewrite-commits](https://github.com/f/git-rewrite-commits)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111205.webp)

Công cụ sử dụng AI để viết lại các thông điệp commit cũ trên git, giúp chúng trở nên chính xác và chi tiết hơn.

## Tài nguyên

1、[Top 100 ảnh tiêu biểu của năm](https://time.com/7336112/top-100-photos-2025/)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112901.webp)

Tạp chí Time bình chọn 100 bức ảnh của năm 2025. Bạn cũng có thể xem [ảnh tiêu biểu của Reuters](https://www.reuters.com/investigates/special-report/year-end-2025-photos-best/).

2、[Những bài viết được đọc nhiều nhất trên Wikipedia năm 2025](https://wikimediafoundation.org/news/2025/12/02/announcing-wikipedias-most-read-articles-of-2025/)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120303.webp)

Wikipedia công bố 20 bài viết tiếng Anh được đọc nhiều nhất năm 2025, chủ yếu xoay quanh chính trị, văn hóa đại chúng và những người vừa qua đời.

3、[HummingbirdSpot](https://hummingbirdspot.com/all-hummingbird-species/)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112707.webp)

Website của một nữ giáo viên Mỹ đã nghỉ hưu với quyết tâm chụp ảnh mọi loài chim ruồi. Thế giới có 366 loài, bà đã chụp được 277 loài.

## Hình ảnh

1、[Bảo tàng Hoàng tử bé](https://www.lepetitprince.com/en/events-around-the-world/a-new-little-prince-museum-has-opened-its-doors-in-switzerland/)

Cuốn truyện kinh điển “Hoàng tử bé” xuất bản năm 1943 đã chinh phục độc giả toàn thế giới.

Để kỷ niệm cuốn sách này và tác giả Saint-Exupéry, Thụy Sĩ vừa khai trương một Bảo tàng Hoàng tử bé mới.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025113001.webp)

Bảo tàng này trưng bày nhiều phiên bản khác nhau của cuốn truyện cùng các kỷ vật liên quan.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025113002.webp)

Cốt truyện của “Hoàng tử bé” kể về hành trình của một hoàng tử sống trên tiểu hành tinh B612. Tiểu hành tinh này rất nhỏ, chỉ có hai ngọn núi lửa đang hoạt động, một ngọn núi lửa tắt và một bông hồng.

Sau khi rời B612, hoàng tử bé đã ghé thăm sáu tiểu hành tinh khác, nơi ở của một nhà vua, một gã hợm hĩnh, một tay nát rượu, một nhà kinh doanh, một người thắp đèn và một nhà địa lý. Cuối cùng, hoàng tử bé đến Trái Đất và sau chuyến viếng thăm đã quay trở về hành tinh của mình.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025113003.webp)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025113004.webp)

## Trích dẫn

1、[Tại sao chất lượng mã nguồn ở các công ty lớn lại kém?](https://www.seangoedecke.com/bad-code-at-big-companies/)

Trái với suy nghĩ của nhiều người, chất lượng mã nguồn tại các công ty lớn thực tế không hề cao.

Điều này nghe có vẻ phi lý. Các tập đoàn công nghệ lớn trả lương rất hậu hĩnh, đủ sức thu hút những kỹ sư giỏi nhất. Hơn nữa, môi trường làm việc, công cụ hỗ trợ và nhịp độ phát triển ở đó đều rất lý tưởng để tạo ra những sản phẩm chất lượng cao một cách ung dung.

Nhưng sự thật là chất lượng mã nguồn của họ chẳng thể gọi là xuất sắc.

Lý do rất đơn giản: phần lớn mã nguồn tại các công ty lớn được viết bởi những người “mới vào nghề” trong lĩnh vực đó.

Không phải các kỹ sư đó kém cỏi, mà là họ bị buộc phải làm những dự án ngoài chuyên môn của mình, nên họ trở thành những người mới.

Trong thực tế, các kỹ sư tại những công ty công nghệ lớn hiếm khi gắn bó mãi mãi. Các gói lương thưởng thường được thiết kế cho nhiệm kỳ bốn năm. Sau khi nhận hết cổ phiếu thưởng ban đầu, thu nhập của kỹ sư có thể giảm mạnh. Nếu không được thăng chức, rõ ràng họ sẽ cân nhắc việc ra đi.

Tình hình còn tệ hơn nếu tính đến việc luân chuyển nội bộ. Bản thân tôi chưa bao giờ ở lại một nhóm hay một dự án nào quá ba năm. Sau đó, ít nhất mỗi năm một lần tôi lại trải qua việc tái cơ cấu, đổi nhóm hoặc đổi dự án.

Dĩ nhiên, mã nguồn của các công ty lớn không có tuổi thọ ngắn như vậy. Nhiều kho lưu trữ nội bộ có tuổi đời cả thập kỷ. Vấn đề là qua bao nhiêu năm, các kho này đã qua tay rất nhiều người chủ khác nhau. Các kỹ sư thay nhau “mày mò” khiến một tỷ lệ lớn các thay đổi được thực hiện bởi những “người mới”. Họ có thể chỉ mới gia nhập công ty hoặc tiếp cận dự án trong vòng sáu tháng trở lại đây.

Bạn chắc chắn sẽ thắc mắc, vậy những lập trình viên “lão làng” không viết code sao? Luôn có những kỹ sư làm việc đủ lâu trong một lĩnh vực cụ thể để tích lũy kiến thức chuyên sâu thực sự. Họ có thể thực hiện những cuộc rà soát mã nguồn kỹ lưỡng và phát hiện ra vấn đề. Vậy họ đang làm gì?

Thứ nhất, các công ty lớn không quan tâm đến kỹ sư “lão làng”. Họ hiếm khi nỗ lực bồi dưỡng nhân tài gắn bó lâu dài với một chuyên môn cụ thể, và dường như cũng chẳng mặn mà việc giữ chân họ. Thông thường, sớm muộn gì những người này cũng bị điều sang bộ phận khác và lại trở thành “người mới” trong một hệ thống hoàn toàn xa lạ.

Thứ hai, các kỹ sư “lão làng” luôn trong tình trạng quá tải. Là số ít người am hiểu tường tận về một dịch vụ nhất định, công việc của họ cực kỳ bận rộn. Họ không đủ thời gian để tự tay rà soát mọi thay đổi phần mềm hay tham gia sâu sát vào từng quyết định. Họ còn có công việc riêng phải hoàn thành.

Tóm lại, thực tế ở các công ty lớn là bạn luôn bị giao cho dự án mới và hầu như ngày nào cũng phải chạy đua để kịp thời hạn của nhiều dự án khác nhau. Nói cách khác, các kỹ sư đang nỗ lực hết mình trong một môi trường không hề thuận lợi để viết ra những dòng mã chất lượng cao.

Trong hoàn cảnh đó, rất khó để đảm bảo chất lượng mã nguồn tốt. Phổ biến nhất là cảnh một kỹ sư cấp thấp tiếp quản một ticket sửa lỗi khó chịu trong một dự án mà anh ta chẳng mấy quen thuộc. Anh ta mất vài ngày nghiên cứu và cuối cùng đưa ra một giải pháp chắp vá. Nếu may mắn, một “lão làng” sẽ dành ra nửa giờ rảnh rỗi để lướt qua, bác bỏ phương án đó và gợi ý một cách khác khá hơn một chút, ít nhất là có thể chạy được. Kỹ sư cấp thấp cố gắng thực hiện theo, kiểm tra xem nó có hoạt động không, rồi sau một cuộc rà soát sơ sài, giải pháp được tung ra. Mọi người liên quan lập tức chuyển sang giải quyết công việc ưu tiên cao tiếp theo.

## Ý kiến


Người dân châu Á đang trong quá trình chuyển dịch từ cuộc sống nông nghiệp khắc nghiệt sang đời sống công xưởng đô thị. Sự chuyển dịch này dường như mang lại một niềm hăng say, một sự sẵn lòng làm việc chăm chỉ vì những thứ mà ở châu Âu ngày nay bị coi là tầm thường.

Đó là điều tốt cho họ. Nhưng ở châu Âu, chúng ta đã trải qua quá trình này rồi, giờ đây trở nên nhàn rỗi và mất hết nhu khí. Khi mọi thứ cần thiết cho cuộc sống đều do người khác làm ra, tình trạng này sẽ không thể kéo dài mãi.

-- [Một độc giả Hacker News người Đức](https://news.ycombinator.com/item?id=46072570)


Màn hình điện tử trên ô tô rất có hại khi dùng vào ban đêm, đặc biệt là với những người trên 40 tuổi. Thị lực của họ bắt đầu giảm, khả năng điều tiết và phản ứng với ánh sáng chậm lại. Việc sử dụng màn hình điện tử sẽ làm thay đổi khả năng nhìn đêm, khiến họ khó quan sát rõ con đường phía trước.

-- [Độc giả Hacker News](https://news.ycombinator.com/item?id=46092397)


Người bình thường không đọc hiểu được các bài báo toán học. Nhưng điều mà người ngoài không biết là, chính các nhà toán học cũng không hiểu nổi nhiều bài báo toán học của đồng nghiệp.

-- [Tạp chí Science](https://www.science.org/doi/10.1126/science.aec9014)


Trong kỷ nguyên của các mô hình lớn, chúng ta đang dần đánh mất một thứ quý giá: giọng nói độc nhất của chính mình.

Mọi bài viết do AI tạo ra đều nghe như thể được phát hành bởi cùng một người quản lý truyền thông công cộng.

Nếu bạn để AI viết mọi thứ cho mình, bạn đang từ bỏ giọng nói riêng của bản thân. Giọng nói của bạn là một tài sản, được nhào nặn từ kinh nghiệm sống cả cuộc đời. Không có ai sở hữu giọng nói hoàn toàn giống bạn cả.

-- [“Các mô hình lớn đang làm chúng ta mất đi giọng nói”](https://tonyalicea.dev/blog/were-losing-our-voice-to-llms/)

(Hết)
