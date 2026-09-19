---
date: 2026-09-18
tags: ["react-native", "mobile", "di động", "ai", "trí tuệ nhân tạo", "lập trình", "programming", "bản đồ", "mã nguồn mở", "phần mềm"]
---

# Tạm biệt, React Native

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026091701.webp)

Cổng phía tây mới khánh thành tại khuôn viên Mẫn Hàng của Đại học Sư phạm Hoa Đông, được phục dựng theo thiết kế cổng trường Đại học Quang Hoa, một trong những tiền thân của trường. ([via](https://www.ecnu.edu.cn/info/1426/73055.htm))

## Tạm biệt, React Native

Shopify vừa [công bố](https://shopify.engineering/back-to-native) quyết định từ bỏ React Native để quay lại dùng Swift và Kotlin phát triển ứng dụng di động.

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026091307.webp)

Nói cách khác, họ chọn quay lại với ngôn ngữ native để phát triển ứng dụng cho iOS và Android, thay vì tiếp tục dựa vào công nghệ Web để dựng một phiên bản trung gian rồi mới biên dịch sang từng nền tảng.

Quyết định này khiến nhiều người nhớ lại chuyện 6 năm trước, vào năm 2020, chính Shopify từng đăng [một bài viết](https://shopify.engineering/react-native-future-mobile-shopify) rầm rộ tuyên bố từ bỏ native, chuyển hoàn toàn sang React Native để đón nhận thế giới Web.

Thời điểm ấy, đây là tin chấn động làng công nghệ. Không ít người gật gù tán đồng với ba lý do mà họ đưa ra:

> - Không phải viết lại cùng một tính năng cho từng nền tảng riêng biệt.
> - Cho phép kỹ sư làm việc linh hoạt trên nhiều stack công nghệ.
> - Tiết kiệm thời gian và công sức để tập trung tạo ra nhiều giá trị hơn.

Thành thật mà nói, ba lý do trên chỉ là lời hoa mỹ, lý do thực sự duy nhất chỉ gói gọn trong hai chữ: tiết kiệm tiền.

Năm xưa chọn React Native là để cắt giảm chi phí. Thay vì phải duy trì hai đội ngũ riêng biệt cho iOS và Android, họ chỉ cần nuôi một team duy nhất, tiết kiệm được một khoản ngân sách khổng lồ.

Bây giờ từ bỏ React Native, trớ trêu thay, cũng là để tiết kiệm tiền. Khi AI đã hiện diện ở khắp nơi, việc bạn viết bằng ngôn ngữ nào dường như không còn quan trọng. AI dịch chuyển code giữa các ngôn ngữ một cách dễ dàng, vậy thì tội gì không dùng luôn ngôn ngữ native để đạt hiệu năng tối đa và bỏ hẳn tầng trung gian?

Tất nhiên, bản thân React Native cũng có phần hụt hơi. Ra mắt từ năm 2015, chặng đường hơn một thập kỷ trôi qua nhưng một số vấn đề kỹ thuật cốt lõi vẫn chưa được giải quyết triệt để, trải nghiệm bắt đầu dự án cũng chẳng mấy dễ chịu. Bị thay thế lúc này, nói thẳng ra, chẳng oan ức chút nào.

Nói tóm lại, AI giống như một cỗ máy thông dịch vạn năng. Khi cỗ máy ấy xuất hiện, những tầng trung gian hay ngôn ngữ bắc cầu như React Native gần như nhận bản án tử, việc chúng dần lùi vào dĩ vãng là cái kết khó tránh khỏi.

## Phép chiếu bản đồ thế giới mới

Tuần trước vừa diễn ra một sự kiện đáng chú ý: Liên Hợp Quốc bỏ phiếu thông qua quyết định [khai tử](https://www.not-ship.com/united-nations-map/) phép chiếu Mercator.

Nghị quyết này không mang tính ràng buộc pháp lý với các quốc gia, nhưng nó là cột mốc ngầm khẳng định rằng phép chiếu Mercator đã thực sự lỗi thời và cần được thay thế.

Ai cũng biết trái đất hình cầu, còn bản đồ lại phẳng. Muốn đưa bề mặt cong của quả địa cầu lên mặt phẳng, ta buộc phải dùng một phép biến đổi nào đó. Điều này cũng đồng nghĩa với việc bản đồ phẳng luôn luôn có sự sai lệch nhất định.

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026091702.webp)

Hình trên là bản đồ thế giới quen thuộc bấy lâu nay, vẽ theo phép chiếu Mercator.

Phép chiếu này biến quả địa cầu thành một hình chữ nhật. Hệ quả là các khu vực ở vĩ độ cao bị kéo giãn khủng khiếp, khiến diện tích trông lớn hơn thực tế rất nhiều.

Nhìn vào hình, đảo Greenland ở vùng cực trông to ngang ngửa cả lục địa châu Phi ở xích đạo. Thế nhưng trên thực tế, diện tích châu Phi lớn gấp 14 lần Greenland.

Liên Hợp Quốc khuyến nghị từ bỏ phép chiếu Mercator và **chuyển sang phép chiếu Equal Earth (Equal Earth Projection) để vẽ bản đồ thế giới**.

Nguyên tắc cốt lõi của phép chiếu Equal Earth là bảo toàn tỷ lệ diện tích. Nếu một vùng đất chiếm 1% bề mặt trái đất, nó cũng sẽ chiếm đúng 1% diện tích trên bản đồ, tỷ lệ diện tích vì thế hoàn toàn chuẩn xác.

Đánh đổi lại, hình dạng của các vùng đất sẽ bị biến dạng. Ở vùng xích đạo và vĩ độ thấp, bản đồ bị kéo giãn theo chiều dọc bắc nam và hơi co lại theo chiều đông tây. Ngược lại ở hai cực và vĩ độ cao, bản đồ nở rộng theo chiều ngang và dẹp bớt theo chiều dọc.

Do đó, phép chiếu này làm biến dạng hình dáng thực tế của các lục địa, cả chiều dài lẫn chiều rộng đều thay đổi, bạn không thể dùng loại bản đồ này để định vị hay dẫn đường chính xác.

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026091305.webp)

Bản đồ thế giới theo phép chiếu Equal Earth ở hình trên cho thấy châu Phi đã trở về đúng tầm vóc thật của mình.

Dưới đây là hình ảnh so sánh châu Âu và châu Phi giữa phép chiếu Mercator và phép chiếu Equal Earth để bạn thấy rõ sự khác biệt.

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026091306.webp)

## Tin tức công nghệ

1\. [Thiết bị phát hiện camera ẩn](https://www.chosun.com/english/industry-en/2026/08/30/SBFXUIJQYZEARKP5T4FBAY25HQ/)

Bạn có bao giờ lo lắng liệu xung quanh mình có camera quay lén hay không?

Các nhà khoa học Hàn Quốc vừa phát minh một thiết bị nhỏ gọn, giúp nhanh chóng phát hiện các mắt camera giấu kín ở môi trường xung quanh.

Cấu tạo của nó đơn giản chỉ là một bảng mạch gắn nhiều đèn LED chiếu sáng tuần tự. Bạn chỉ cần cắm vào điện thoại là dùng được ngay, chi phí sản xuất cực kỳ rẻ.

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026090101.webp)

Nguyên lý hoạt động dựa trên việc ánh sáng phát ra từ đèn LED sẽ phản chiếu lại từ ống kính camera ẩn. Bằng cách lọc bỏ phản xạ từ các mặt gương thông thường trong chùm sáng thu về, thiết bị có thể xác định chính xác vị trí của camera.

Làm thế nào để loại bỏ những ánh sáng phản xạ gây nhiễu khác? Thiết bị giải quyết bằng một cơ chế thông minh: thắp sáng lần lượt các bóng LED ở những vị trí khác nhau.

Ánh sáng phản chiếu từ các vật thể thông thường đến từ gương phẳng, trong khi ống kính camera lại là thấu kính lồi, tạo ra độ lệch vị trí quang học nhất định. Nhờ nguồn sáng thay đổi liên tục, hệ thống dễ dàng nhận biết phản xạ nào bị lệch vị trí, từ đó định vị chính xác vị trí camera.

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026090102.webp)

2\. **Tin vắn**

(1) Lực lượng [Houthi](https://news.ycombinator.com/item?id=49660072) vừa giành được một chiến thắng đáng kinh ngạc, bằng một phương thức tác chiến kỳ lạ bậc nhất lịch sử.

Họ dùng công nghệ làm giả một đoạn ghi âm của chỉ huy đối phương ra lệnh rút quân, rồi nhờ một tài khoản có sức ảnh hưởng trên mạng xã hội Twitter lan truyền đoạn âm thanh đó. Bất ngờ là quân đội đối phương rơi vào hỗn loạn thật sự, giúp Houthi tiến quân thuận lợi và chiếm giữ vị trí với tổn thất tối thiểu.

(2) Laptop bắt đầu ứng dụng công nghệ tản nhiệt thể rắn, loại bỏ hoàn toàn quạt cơ học và chuyển sang dùng các tấm tản nhiệt graphene kết hợp màng đồng.

Nhờ đó, máy tính xách tay có thể được chế tạo siêu mỏng và nhẹ đến khó tin. [Lenovo](https://www.notebookcheck.net/Lenovo-unveils-ThinkBook-AeroBlade-14-inch-laptop-that-weighs-under-830-grams.1388619.0.html) gần đây giới thiệu mẫu laptop ý tưởng 14 inch chỉ nặng vỏn vẹn 830 gram. Thậm chí chiếc MateBook Pro S 14 inch của Huawei còn nhẹ hơn, chỉ 798 gram.

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026091201.webp)

(3) Thành phố Thành Đô (Trung Quốc) dự kiến triển khai chương trình phát hành "[phiếu trợ cấp token](https://finance.sina.cn/2026-09-11/detail-inirnhrv2204082.d.html?vt=4)". Các cơ quan, doanh nghiệp có thể đăng ký miễn phí, với mức hỗ trợ tối đa 30% chi phí tiêu thụ token cho mô hình ngôn ngữ lớn.

Ngoài ra, thành phố này còn lên kế hoạch ra mắt gói "vay vốn token", cho phép doanh nghiệp vay ngân hàng để chi trả chi phí sử dụng token AI.

## Bài viết

1\. [Bộ khung mẫu HTML của tôi](https://vale.rocks/posts/html-boilerplate) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026091303.webp)

Tác giả giải thích cặn kẽ cấu trúc một mẫu HTML chuẩn chỉnh vào năm 2026 nên được thiết kế thế nào, cùng ý nghĩa chi tiết của từng dòng mã.

2\. [Cách vô hiệu hóa CSS bằng JavaScript](https://css-tricks.com/that-time-i-tried-browsing-the-web-without-css/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025062102.webp)

Bài hướng dẫn cơ bản chỉ cho bạn cách tắt toàn bộ stylesheet CSS của một trang web bằng JavaScript.

3\. [Công cụ quản lý container và reverse proxy](https://web.archive.org/web/20250401115923/https://kiranet.org/posts/self-hosting-like-its-2025/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202504/bg2025040105.webp)

Tác giả chia sẻ kinh nghiệm tự dựng máy chủ cá nhân bằng công nghệ container, cùng toàn bộ tech stack và các công cụ thực tế mà anh sử dụng.

4\. [Những điều kỳ lạ trong JavaScript](https://stack-auth.com/blog/on-javascripts-weirdness) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202504/bg2025040501.webp)

Một bài viết thú vị điểm lại những hành vi kỳ quặc và dễ gây nhầm lẫn ít ai để ý trong cú pháp JavaScript.

5\. [Tham số udm trong tìm kiếm Google](https://serpapi.com/blog/every-google-udm-in-the-world/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025062107.webp)

URL tìm kiếm của Google cho phép bạn gắn thêm tham số `udm` để lọc kết quả theo định dạng mong muốn, chẳng hạn `udm=2` sẽ chỉ trả về kết quả hình ảnh.

6\. [Giải thích khái niệm entropy](https://www.engineersedge.com/thermodynamics/entropy_explained_with_sheep_15961.htm) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202410/bg2024101406.webp)

Bài viết dài sử dụng ngôn ngữ trực quan, dễ hiểu kèm nhiều hình minh họa để làm sáng tỏ khái niệm "entropy" vốn khá trừu tượng trong nhiệt động lực học.

## Công cụ

1\. [Great Tables](https://github.com/posit-dev/great-tables)

![](https://cdn.beekka.com/blogimg/asset/202404/bg2024040402.webp)

Thư viện Python hỗ trợ thiết kế và tạo các bảng biểu trực quan phức tạp nhưng đẹp mắt.

2\. [ghostty-web](https://github.com/coder/ghostty-web)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120214.webp)

Dự án biên dịch trình giả lập terminal [Ghostty](https://ghostty.org/) sang WebAssembly (WASM), cho phép bạn trải nghiệm một terminal đầy đủ tính năng ngay trên trình duyệt web.

3\. [Infat](https://github.com/philocalyst/infat)

Công cụ dòng lệnh trên macOS giúp thiết lập ứng dụng mở mặc định cho các tệp tin theo phần mở rộng.

4\. [mini-img-editor](https://github.com/xdadda/mini-photo-editor)

![](https://cdn.beekka.com/blogimg/asset/202504/bg2025042901.webp)

Trình chỉnh sửa ảnh trực tuyến xây dựng bằng WebGL, đóng vai trò bản demo giao diện mẫu với thiết kế gọn gàng, tinh tế.

5\. [CryptPad](https://cryptpad.fr/)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025050101.webp)

Bộ ứng dụng văn phòng trực tuyến miễn phí hỗ trợ mã hóa đầu cuối (end-to-end), xem thêm [bài viết giới thiệu](https://www.xda-developers.com/reasons-why-use-cryptpad-instead-google-docs/).

6\. [Lyrimuse](https://github.com/Yudaotor/lyrimuse)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026091308.webp)

Tiện ích hiển thị lời bài hát trên desktop dành cho macOS, tự động tìm kiếm và đồng bộ lời theo thời gian thực cho bài hát đang phát. (Đóng góp từ [@Yudaotor](https://github.com/ruanyf/weekly/issues/11551))

7\. [capcut-cli](https://github.com/renezander030/capcut-cli)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026091619.webp)

Công cụ dòng lệnh không chính thức dành cho CapCut, giúp bạn tạo và dựng video trực tiếp từ terminal. (Đóng góp từ [@renezander030](https://github.com/ruanyf/weekly/issues/11634))

8\. [mailez](https://github.com/mailez-hq/mailez)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026091621.webp)

Tệp nhị phân viết bằng Go giúp tự dựng hệ thống mail cá nhân (self-hosted), hỗ trợ giao diện web để gửi nhận thư, tương thích cùng lúc 4 giao thức SMTP, IMAP, POP3 và ManageSieve. (Đóng góp từ [@lianguan](https://github.com/ruanyf/weekly/issues/11680))

9\. [Status Trio](https://github.com/lingyired/status-trio)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026091622.webp)

Tiện ích thanh trạng thái macOS kết hợp ba trong một, lấy cảm hứng từ phong cách Dynamic Island của iPhone, tích hợp theo dõi Wi-Fi, pin và âm lượng. (Đóng góp từ [@lingyired](https://github.com/ruanyf/weekly/issues/11670))

10\. [Polycompiler](https://github.com/EvanZhouDev/polycompiler)

Một dự án thú vị cho phép đóng gói đồng thời script JavaScript và script Python vào chung một tệp lệnh duy nhất, có thể thực thi trơn tru trong cả môi trường JS lẫn Python.

## Tài nguyên

1\. [gpcb.net](https://gpcb.net/net/)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026091620.webp)

Công cụ trực tuyến hỗ trợ vẽ và thiết kế sơ đồ topo mạng trực quan trên nền web. (Đóng góp từ [@abpyu](https://github.com/ruanyf/weekly/issues/11622))

2\. [Bách khoa phong cách thị giác](https://ruanyf.github.io/squoosh/editor)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026091309.webp)

Bộ sưu tập sử dụng hình ảnh một quả táo để minh họa cho hơn 100 phong cách mỹ thuật và thị giác khác nhau, chẳng hạn hình trên là quả táo theo phong cách neon. (Đóng góp từ [@jerrymakes](https://github.com/ruanyf/weekly/issues/11555))

3\. [Kiểm tra IP kết nối AI](https://store.xiu.ai/zh/ai-ip/)

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026091407.webp)

Trang web giúp bạn kiểm tra địa chỉ IP thực tế mà mình đang kết nối tới khi truy cập các dịch vụ như Claude, ChatGPT, Grok, Perplexity hay Cloudflare. (Đóng góp từ [@MuduiClaw](https://github.com/ruanyf/weekly/issues/11571))

4\. [Trọng lực](https://qunabu.github.io/Gravity/#what-is-gravity) (Gravity)

![](https://cdn.beekka.com/blogimg/asset/202606/bg2026062007.webp)

Trang web tương tác đa phương tiện giúp người xem khám phá và tìm hiểu về các định luật vạn vật hấp dẫn một cách sinh động.

## Hình ảnh

1\. [Mũ bay F-35](https://www.instagram.com/p/DJPerYryd3P/)

Chiếc mũ bảo hiểm đắt giá nhất hành tinh thuộc về phi công lái tiêm kích tàng hình F-35 của Mỹ, trị giá lên tới 400.000 USD mỗi chiếc (tương đương khoảng 10 tỷ đồng).

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025050905.webp)

Mức giá đắt đỏ đến từ việc chiếc mũ tích hợp trực tiếp vào hệ thống cảm biến của máy bay, tiếp nhận và xử lý hàng loạt luồng dữ liệu thời gian thực.

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025050906.webp)

Bên trong mũ trang bị màn hình hiển thị 360 độ, cung cấp tầm nhìn ban đêm và toàn bộ thông số bay cần thiết cho phi công (hình dưới).

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025050907.webp)

Mỗi chiếc mũ đều được quét 3D theo đúng kích cỡ đầu của từng phi công, chế tác từ sợi carbon, sợi Kevlar cùng các linh kiện quang học chính xác cao.

2\. [Trực thăng chở khách khổng lồ Mi-6 của Liên Xô](https://www.twz.com/news-features/the-story-of-the-monster-mi-6-helicopter-airliner)

Hãng hàng không Liên Xô từng ấp ủ ý tưởng dùng trực thăng cỡ lớn để vận chuyển hành khách thường xuyên.

Vào những năm 1960, họ chế tạo mẫu trực thăng Mi-6, cỗ máy bay lên thẳng lớn nhất thế giới lúc bấy giờ với sức chứa lên tới 80 hành khách.

![](https://cdn.beekka.com/blogimg/asset/202407/bg2024071115.webp)

![](https://cdn.beekka.com/blogimg/asset/202407/bg2024071116.webp)

Thân máy bay dài khoảng 33 mét, cao 10 mét. Khoang hành khách bố trí 5 ghế mỗi hàng, thậm chí trang bị cả nhà vệ sinh riêng.

![](https://cdn.beekka.com/blogimg/asset/202407/bg2024071117.webp)

Dù vậy, phiên bản chở khách này chỉ sản xuất duy nhất một chiếc, chuyên dùng đưa đón công nhân và kỹ sư đến các mỏ dầu khí ở vùng viễn đông xa xôi của Liên Xô.

![](https://cdn.beekka.com/blogimg/asset/202407/bg2024071118.webp)

## Trích đoạn

1\. [Món lasagna bầy hầy](https://underreacted.leaflet.pub/3mdjygm2p5s2c)

Nói thẳng ra thì trong thực tế, code của đa số lập trình viên viết ra đều khá tệ.

Thế nhưng code tệ cũng có dăm bảy loại. Tệ nhất là mớ bòng bong kiểu mì spaghetti (spaghetti code), mọi thứ chằng chịt quấn lấy nhau đến mức không ai gỡ nổi.

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026090704.webp)

Đỡ hơn một bậc là kiểu "[lasagna bầy hầy](https://underreacted.leaflet.pub/3mdjygm2p5s2c)" (slop lasagna). Dù chất lượng từng phần bên trong có nhão nhoẹt, ít nhất nó vẫn được chia thành từng lớp rõ ràng, bạn hoàn toàn có thể tách từng lớp ra xử lý.

![](https://cdn.beekka.com/blogimg/asset/202609/bg2026090703.webp)

Kể cả khi bạn chưa thể viết ra thứ code mẫu mực hoàn hảo, **bạn vẫn nên cố gắng tránh xa mã nguồn kiểu mì spaghetti và hướng tới cấu trúc bánh lasagna nhiều tầng**.

Minh chứng điển hình chính là React. Framework này chia nhỏ giao diện thành các component độc lập. Điểm hay ho là dù code bên trong một component có tệ hại đến đâu, bạn vẫn có thể cô lập và thay thế riêng component đó mà không làm sụp đổ toàn bộ hệ thống.

Xóa bớt component, sao chép component, inline hay viết lại từ đầu đều rất nhẹ nhàng. Nhờ ranh giới rõ ràng, tâm trí bạn chỉ cần dồn vào **duy nhất một component** tại một thời điểm.

Miễn là cây component được thiết kế mạch lạc, việc bên trong một component viết vụng về ra sao không còn là thảm họa. Ai đó lỡ tay viết một component rác dài 10.000 dòng thì đã sao? Sớm muộn cũng sẽ có người đập đi viết lại, nó chẳng thể lây lan làm hỏng phần còn lại của codebase.

**Chỉ cần mã nguồn giữ được cấu trúc phân tầng kiểu lasagna, một tầng có tệ cũng không kéo đổ cả công trình**.

Những thứ thực sự đáng để bạn bận tâm là:

(1) Dữ liệu luân chuyển trong hệ thống ra sao, đầu vào từ đâu tới, đầu ra tạo ra những gì, và bạn đang lưu trữ dữ liệu nào.

(2) Trải nghiệm người dùng thế nào, có lỗ hổng nghiêm trọng, tụt giảm hiệu năng hay hành vi thiếu nhất quán hay không.

(3) Các trừu tượng hóa nền tảng có chuẩn xác không, có bị lạm dụng hay hiểu sai bản chất không.

**Chỉ cần ba yếu tố trên ổn thỏa, cộng thêm kiến trúc module hóa theo component dễ tháo lắp, chương trình sẽ không gặp vấn đề lớn**. Khi ấy, việc một vài component có hơi dài dòng, viết chưa sạch đẹp hay còn dính vài lỗi vặt cũng chẳng ảnh hưởng tới cục diện chung.

## Trích dẫn

1\.

Vệ tinh sẽ tiêu hao dần năng lượng tự quay của hành tinh mẹ, qua đó đẩy nhanh quá trình diệt vong của hành tinh đó.

-- [Sao Kim có từng nuốt chửng mặt trăng của chính mình?](https://www.space.com/astronomy/venus/did-venus-eat-its-own-moon)

2\.

Thử tưởng tượng hai công ty phần mềm gần như y hệt nhau: doanh thu tương đương, sản phẩm cung cấp cũng tương đồng. Điểm khác biệt duy nhất là công ty A vận hành với 1 triệu dòng code, còn công ty B chỉ cần 100.000 dòng code. Công ty nào sẽ phát triển tốt hơn?

Rõ ràng bên chỉ sở hữu lượng code bằng một phần mười sẽ chiếm ưu thế vượt trội. Càng ít code, bạn càng thấu hiểu và sửa đổi hệ thống nhanh hơn bấy nhiêu.

-- [Code chính là nợ kỹ thuật](https://tornikeo.com/code-is-debt/)

3\.

Các mô hình ngôn ngữ lớn sẽ biến bạn từ một lập trình viên cặm cụi gõ code thành người quản lý ngữ cảnh, loại bỏ thông tin rác và trau chuốt từng câu prompt tỉ mỉ.

-- [Liz Fong-Jones](https://simonwillison.net/2025/Dec/30/liz-fong-jones/)

4\.

Một nhà sáng lập nếu vào năm 2024 tập hợp được đúng đội ngũ nhưng làm ra sản phẩm chưa phù hợp, chỉ cần kiên trì đến năm 2027, nhóm của anh ấy sẽ tôi luyện thành một tập thể dày dạn kinh nghiệm thực chiến và hoàn toàn đủ sức tạo nên sản phẩm trúng đích.

Bài học từ thất bại giống như chất dinh dưỡng được gom lại trong rễ cây, âm thầm tích lũy để chờ đón mùa xuân kế tiếp đơm hoa kết trái, chứ không hề uổng phí.

-- [AI sẽ không sụp đổ, nhưng phải vượt qua một cơn bão](https://ceodinner.substack.com/p/the-ai-wildfire-is-coming-its-going)

5\.

Nhiều công nghệ gặp trục trặc chẳng phải vấn đề gì quá ghê gớm. GPS dẫn đường sai, bạn phát hiện ra ngay khi nhìn cảnh quan; Netflix gợi ý phim dở, bạn bấm tắt chuyển phim khác.

Thế nhưng AI lại là câu chuyện hoàn toàn khác. Mô hình càng tối tân, ta càng khó nhận biết khi nào nó mắc lỗi, bởi chúng ta đang giao cho AI những nhiệm vụ vượt quá tầm hiểu biết hoặc khả năng tự kiểm chứng của con người.

Một khi AI sai phạm, ta chỉ còn biết liên tục triệu hồi một mô hình AI mạnh hơn nữa với hy vọng câu thần chú mới sẽ linh nghiệm. Chào mừng bạn đến với thời đại của những pháp sư phù thủy.

-- [Làm việc với AI như làm việc với pháp sư](https://www.oneusefulthing.org/p/on-working-with-wizards)
