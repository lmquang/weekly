# Một lỗi của cánh cửa

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112516.webp)

Bảo tàng Nghệ thuật Đương đại Tô Châu sắp mở cửa. Mái nhà của mười phòng triển lãm nối liền nhau, tượng trưng cho những mái ngói của nhà dân vùng Giang Nam. ([via](https://www.archiposition.com/items/29335ee2bf))

## Một lỗi của cánh cửa

Bạn đã bao giờ nghe về những lỗi phần mềm kỳ lạ nhất chưa?

[Câu chuyện dưới đây](https://mastodon.gamedev.place/@TomF/115589875974658415) tôi mới đọc tuần này, chắc chắn nằm trong top 10 những lỗi kỳ quặc nhất lịch sử.

Tôi dịch lại để chia sẻ với mọi người, lời kể dưới góc nhìn thứ nhất:

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112518.webp)

Năm 2013, tôi làm phát triển trò chơi tại Valve.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112201.webp)

Lúc đó, kính thực tế ảo VR thế hệ đầu tiên Oculus DK1 vừa ra mắt. Công ty quyết định đưa trò chơi lên thiết bị này và giao cho tôi phụ trách để tìm hiểu môi trường trò chơi VR.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112202.webp)

Tôi chọn Half-Life 2, một trò chơi chúng tôi phát triển từ năm 2004, để thực hiện.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112203.webp)

Sau khi thử nghiệm một đoạn và thấy hiệu quả rất tốt, chúng tôi quyết định chuyển đổi toàn bộ trò chơi và tung ra trailer giới thiệu.

Trong quá trình thực hiện, tôi chơi thử rất nhiều phân đoạn nhưng chưa bao giờ chơi từ đầu đến cuối một mạch.

Khi mọi thứ hoàn tất, ngay sát ngày phát hành, tôi quyết định chơi lại toàn bộ. Nếu phát hiện vấn đề gì, tôi sẽ ghi chú vào phần hướng dẫn phát hành.

Tôi nghĩ bụng chắc sẽ không có vấn đề lớn đâu. Trò chơi này ra mắt 10 năm rồi, hàng triệu người đã chơi và phản hồi rất tốt.

Nhưng tôi không ngờ mình lại gặp một Bug nghiêm trọng.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112205.webp)

Ở phần đầu trò chơi, khi người chơi đến ga tàu, một lính canh bảo bạn đi vào một căn phòng. Kỳ lạ là cửa phòng đóng chặt. Bạn không thể vào và thế là bị kẹt.

Nhân vật không chết, chỉ là không đi đâu được. Cửa trước đóng, lối sau cũng đã khóa. Bạn bị nhốt trong một hành lang với một tên lính canh bên cạnh, không còn đường thoát. Thật kỳ quặc.

Theo cốt truyện, bạn phải vào căn phòng đó mới có thể tiếp tục. Bạn quay lại hỏi lính canh, hắn chỉ tay vào cánh cửa đang khóa, thế thôi. Bạn hoàn toàn bế tắc.

Tôi lên mạng tìm video xem mình có nhớ nhầm không. Đúng là cửa phải tự mở, bạn chỉ việc bước vào. Nhưng bây giờ cánh cửa này lại đóng im lìm!

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112206.webp)

Tôi nghĩ phen này hỏng rồi, không thể phát hành trò chơi được.

Tôi vội liên lạc với những người khác, kể cả những người tham gia phát triển trò chơi mười năm trước. Sau khi kiểm tra, họ xác nhận đúng là có lỗi. Ngay cả ở chế độ không phải VR cũng gặp tình trạng tương tự. Vậy là không phải do quá trình chuyển sang VR của tôi làm hỏng. Nhưng không ai biết nguyên nhân vì mã nguồn không hề thay đổi.

Có người thậm chí còn tìm lại mã nguồn gốc, biên dịch lại phiên bản đầu tiên lúc phát hành. Kết quả là bản gốc đó cũng hỏng, cửa vẫn đóng.

Làm sao chuyện này có thể xảy ra? Mọi người hoảng hốt. Điều này nghĩa là Bug đã tồn tại mười năm trước, nhưng tại sao lúc đó biên dịch lại không xuất hiện, còn bây giờ biên dịch lại thì nó lại hiện ra?

Sau khoảng một ngày dùng các công cụ gỡ lỗi và xem lại từ thời đó, một đồng nghiệp đã tìm ra nguyên nhân.

Nếu quan sát kỹ trò chơi, bạn sẽ thấy cánh cửa đó thực chất đã tự mở và mở ra trong một khoảnh khắc ngắn. Nhưng trong phòng còn có một lính canh thứ hai đứng sau cửa. Tên này đứng quá sát cửa. Khi cửa vừa mở, nó chạm nhẹ vào ngón chân của lính canh, sau đó nảy ngược lại, đóng sập và tự khóa luôn. Vì trò chơi không tính đến trường hợp này để mở lại cửa, nên người chơi bị kẹt.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112207.webp)

Khi đã hiểu chuyện, cách giải quyết rất đơn giản. Chúng tôi lùi tên lính canh lại khoảng một milimét, cánh cửa lập tức mở ra trơn tru.

Bây giờ chúng tôi có thể phát hành trò chơi. Nhưng vấn đề vẫn chưa được giải quyết triệt để. Tại sao ngày xưa không có lỗi này khi ngón chân của lính canh vẫn nằm đó? Tại sao mười năm sau biên dịch lại thì lỗi mới xuất hiện? Hay lỗi vẫn luôn ở đó, nhưng vì sao mười năm trước cửa không bị đóng lại?

Thế là một cuộc truy tìm lỗi quy mô lớn bắt đầu.

Cuối cùng chúng tôi cũng tìm ra đáp án. Đó là câu chuyện cũ rích về tính toán số thực dấu phẩy động (floating point).

Half-Life 2 phát hành năm 2004, lúc đó dùng bộ lệnh toán học cũ 8087 hoặc x87 để biên dịch. Các bộ lệnh này có độ chính xác số thực rất lộn xộn, chỗ thì 32 bit, chỗ thì 64 bit, chỗ lại 80 bit. Các đoạn mã khác nhau dùng độ chính xác khác nhau.

Mười năm sau, vào năm 2013, bộ lệnh SSE đã trở thành tiêu chuẩn cho mọi CPU x86. Trình biên dịch mặc định dùng SSE với độ chính xác rõ ràng (32 bit hoặc 64 bit tùy yêu cầu), mọi thứ đều có thể dự đoán được.

Sự thật là mười năm trước dùng độ chính xác 32 bit, còn bây giờ dùng 64 bit. Sự khác biệt ở phần thập phân tạo ra sai số vài milimét, khiến ngón chân lính canh chạm vào cửa.

Vậy là xong, giờ đây người chơi cuối cùng đã có thể bước qua cánh cửa và tiếp tục hành trình.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112208.webp)

## Tin tức công nghệ

1、[Giảng dạy bằng AI](https://www.theguardian.com/education/2025/nov/20/university-of-staffordshire-course-taught-in-large-part-by-ai-artificial-intelligence)

Sinh viên tại Đại học Staffordshire (Anh) vừa khiếu nại với truyền thông.

Khi lên lớp, các trang slide của giảng viên (hình dưới) hoàn toàn do AI tạo ra. Thậm chí giảng viên còn không trực tiếp giảng bài mà chỉ phát giọng nói do AI tạo ra.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112102.webp)

Sinh viên rất phẫn nộ vì theo quy định của trường, nếu sinh viên nộp bài tập dùng AI sẽ bị đuổi học, nhưng giảng viên lại dùng AI để dạy.

Điều này vừa phản ánh chất lượng giáo dục đại học ở Anh đang đi xuống, vừa khiến người ta phải suy ngẫm. Nếu đại học sử dụng AI rộng rãi để dạy học, hoặc chất lượng giảng dạy của giảng viên không bằng AI, thì sinh viên có cần đến trường nữa không? Tại sao không học trực tiếp từ AI?

2、[Ghế cua](https://mossandfog.com/toyotas-crab-like-wheelchair-that-walks/)

Toyota vừa ra mắt một sản phẩm ý tưởng là chiếc ghế có thể di chuyển như con cua.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111217.webp)

Bốn chân của nó có thể cử động nhờ các khớp nối điều khiển bằng động cơ điện. Người ngồi trên đó sẽ được ghế tự đưa đi, thậm chí là leo bậc thang.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111219.webp)

Nó còn có thể nằm xuống và đứng dậy.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111220.webp)

Tôi dự đoán thị trường robot vận chuyển người ngồi như thế này sẽ rất lớn, và sớm muộn gì cũng có những sản phẩm tương tự ra đời.

3、[Máy tính lượng tử](https://www.ianvisits.co.uk/articles/you-can-see-a-working-quantum-computer-in-ibms-london-office-85464/)

Văn phòng IBM tại London đang trưng bày một chiếc máy tính lượng tử.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112503.webp)

Chiếc máy này chế tạo năm 2019 và hiện đã lỗi thời. Tuy nhiên, bạn không thể vào tận nơi xem mà chỉ được đứng nhìn từ xa ở cửa.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112506.webp)

Thiết bị này được coi là tương lai của máy tính, có khả năng bẻ khóa các thuật toán mã hóa hiện nay rất nhanh. Tuy nhiên, nó cần môi trường làm việc cực lạnh, gần độ không tuyệt đối, nên không thể sử dụng tại nhà.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112504.webp)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112505.webp)

4、[Chi phí cho website chính phủ](https://www.abc.net.au/news/2025-11-23/bureau-of-meteorology-new-website-cost-blowout-to-96-million/106042202)

Xây dựng một website chính phủ tốn bao nhiêu tiền? Câu trả lời là 96,5 triệu đô la Úc (khoảng 450 triệu nhân dân tệ).

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112514.webp)

Website mới của Cục Khí tượng Úc có chi phí thiết kế 4,1 triệu đô la, chi phí phát triển 79,8 triệu đô la, chi phí phát hành và kiểm tra an ninh là 12,6 triệu đô la. Tổng cộng là 96,5 triệu đô la Úc.

Vì con số này vượt xa ngân sách 4,1 triệu đô la ban đầu nên khi bị truyền thông phanh phui, công chúng đã vô cùng sửng sốt.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112515.webp)

Nực cười hơn là sau khi website mới ra mắt, nông dân phản ánh họ không tìm thấy dữ liệu lượng mưa, buộc phải quay lại dùng website bản cũ.

Làm sao để hệ thống máy tính chính phủ vừa hiệu quả, dễ dùng mà không lãng phí tiền thuế của dân vẫn là một bài toán khó.

Bạn có thể ghé thăm website trị giá 450 triệu tệ này tại [bom.gov.au](https://www.bom.gov.au/). Ngoài ra, [bản cũ](https://reg.bom.gov.au/) hiện vẫn đang hoạt động.

## Bài viết

1、[Tại sao mọi cơ sở dữ liệu đều dùng B-tree](https://mehmetgoekce.substack.com/p/b-trees-why-every-database-uses-them) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112401.webp)

Một bài viết phổ biến kiến thức về lý do tại sao cấu trúc B-tree lại phù hợp cho cơ sở dữ liệu hơn là cây nhị phân.

2、[Tại sao đánh giá mô hình mới ngày càng khó](https://simonwillison.net/2025/Nov/24/claude-opus/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112508.webp)

Lập trình viên nổi tiếng Simon Willison cảm thán rằng ông không còn khả năng đánh giá các mô hình lớn mới nhất nữa. Vì năng lực của các mô hình ngày càng mạnh, những câu hỏi đơn giản đều giải được, nên phải dùng những đề bài cực khó để kiểm tra.

3、[Ổ cứng SSD không được để mất điện quá lâu](https://www.xda-developers.com/your-unpowered-ssd-is-slowly-losing-your-data/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112509.webp)

Bài viết chỉ ra rằng ổ cứng SSD tiêu dùng nếu ở trạng thái mất điện quá một năm sẽ bắt đầu mất dữ liệu.

Hiện tại, ngay cả những ổ SSD tốt nhất cũng không thể chịu được trạng thái mất điện quá mười năm. Vì vậy, nếu không sử dụng trong thời gian dài, bạn đừng lưu trữ dữ liệu quan trọng trong ổ SSD.

4、[Kiểm tra hiệu năng chip Loongson của Trung Quốc](https://lemire.me/blog/2025/11/23/how-good-are-chinese-cpus-benchmarking-the-loongson-3a6000/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112522.webp)

Một lập trình viên nước ngoài thử nghiệm bộ vi xử lý Loongson 3A6000 và so sánh với Intel Xeon Gold 6338 ra mắt năm 2021.

5、[URL bên trong mã nguồn C](https://susam.net/url-in-c.html) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112706.webp)

Đoạn mã C ở trên chứa một URL nhưng vẫn có thể biên dịch được. Tại sao vậy?

6、[Cách tạo một công cụ tìm kiếm đơn giản](https://karboosx.net/post/4eZxhBon/building-a-simple-search-engine-that-actually-works) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112602.webp)

Bài viết giới thiệu nguyên lý của công cụ tìm kiếm và cách tự tay viết một công cụ tìm kiếm đơn giản.

7、[Tự làm NAS: Phiên bản 2026](https://blog.briancmoses.com/2025/11/diy-nas-2026-edition.html) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112708.webp)

Tác giả giới thiệu chi tiết cấu hình tự lắp ráp NAS, bạn có thể tham khảo.

## Công cụ

1、[DNS Benchmark Tool](https://github.com/frankovo/dns-benchmark-tool)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112101.webp)

Công cụ dòng lệnh kiểm tra máy chủ DNS, đo độ trễ từ máy cục bộ đến máy chủ và thời gian phân giải địa chỉ IP của tên miền.

2、[iDescriptor](https://github.com/iDescriptor/iDescriptor)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112405.webp)

Một ứng dụng máy tính đa nền tảng giúp quản lý iPhone kết nối với máy tính.

3、[SVG.js](https://svgjs.dev)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112406.webp)

Thư viện JS cho web dùng để tạo và điều khiển hoạt ảnh hình ảnh SVG.

4、[impala](https://github.com/pythops/impala)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112303.webp)

Một ứng dụng terminal để quản lý WiFi trên nền tảng Linux.

5、[2025-blog-public](https://github.com/YYsuni/2025-blog-public)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112106.webp)

Mẫu website blog tĩnh dựa trên Next.js. ([@YYsuni](https://github.com/ruanyf/weekly/issues/8262) đóng góp)

6、[pdfpc-ts](https://github.com/Master-Hash/pdfpc-ts)

Website mã nguồn mở dùng để trình chiếu slide, có tính năng hiển thị chế độ người thuyết trình để nhắc bài, tương tự ứng dụng [pdfpc](https://github.com/pdfpc/pdfpc). ([@Master-Hash](https://github.com/ruanyf/weekly/issues/8264) đóng góp)

7、[Clip Save](https://github.com/snsogbl/clip-save)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112302.webp)

Phần mềm máy tính mã nguồn mở dùng để lưu lịch sử clipboard, hỗ trợ Windows và Mac. ([@snsogbl](https://github.com/ruanyf/weekly/issues/8269) đóng góp)

8、[Hoa](https://github.com/hoa-js/hoa)

Một framework máy chủ JS lấy cảm hứng từ Koa và Hono, phù hợp cho Cloudflare Worker. ([@nswbmw](https://github.com/ruanyf/weekly/issues/8289) đóng góp)

9、[NodeBBS](https://github.com/aiprojecthub/nodebbs)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112701.webp)

Hệ thống diễn đàn hiện đại mã nguồn mở dựa trên ngôn ngữ JS. ([@wengqianshan](https://github.com/ruanyf/weekly/issues/8294) đóng góp)

10、[MyTube](https://github.com/franklioxygen/MyTube)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112704.webp)

Dịch vụ Web tự vận hành dùng để tải và quản lý video từ hai nền tảng Youtube và Bilibili. ([@franklioxygen](https://github.com/ruanyf/weekly/issues/8300) đóng góp)

## Liên quan đến AI

1、[WeFinance-Copilot](https://github.com/JasonRobertDestiny/WeFinance-Copilot)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112301.webp)

Ứng dụng Web mã nguồn mở giúp người dùng tải lên hóa đơn, sau đó AI sẽ nhận diện và phân tích tài chính. ([@JasonRobertDestiny](https://github.com/ruanyf/weekly/issues/8270) đóng góp)

2、[KoalaQA](https://github.com/chaitin/KoalaQA)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112502.webp)

Hệ thống chăm sóc khách hàng bằng AI mã nguồn mở, có thể dùng xây dựng nền tảng hỏi đáp, cộng đồng nhà phát triển hoặc cộng đồng dịch vụ người dùng. ([@Trc0g](https://github.com/ruanyf/weekly/issues/8286) đóng góp)

3、[seekdb](https://github.com/oceanbase/seekdb)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112521.webp)

Đội ngũ OceanBase ra mắt cơ sở dữ liệu AI mã nguồn mở, hỗ trợ tính toán vector và tương thích với MySQL. ([@liboyang0730](https://github.com/ruanyf/weekly/issues/8288) đóng góp)

4、[OPENUGC](https://chat.openugc.com)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112703.webp)

Ứng dụng web AI client cho phép cấu hình mô hình, Agent và MCP. Tính năng khá đầy đủ nhưng không mã nguồn mở. ([@aicu-icu](https://github.com/ruanyf/weekly/issues/8298) đóng góp)

## Tài nguyên

1、[Hướng dẫn đầy đủ về LangGraph 1.0](https://www.luochang.ink/dive-into-langgraph/quickstart/)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112501.webp)

LangGraph là một framework phát triển Agent mã nguồn mở. Đây là hướng dẫn tương tác dựa trên Jupyter Notebook về cách thực hành với framework này. ([@luochang212](https://github.com/ruanyf/weekly/issues/8283) đóng góp)

2、[Tổng hợp Prompt cho Nano Banana Pro](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts/blob/main/README_zh.md)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112702.webp)

Kho lưu trữ này thu thập hơn 500 Prompt cho mô hình Nano Banana Pro. Mỗi Prompt đều có hình ảnh minh họa và hơn một nửa có kèm thông số. ([@DophinL](https://github.com/ruanyf/weekly/issues/8297) đóng góp)

3、[OCR Arena](https://www.ocrarena.ai)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112507.webp)

Website này là một đấu trường AI nhằm so sánh khả năng OCR (nhận dạng ký tự quang học) của các mô hình khác nhau. Hiện Gemini 3 đang đứng đầu bảng xếp hạng.

## Hình ảnh

1、[Mô hình sân bay](https://www.core77.com/posts/138995/Historically-Accurate-Airport-Dioramas-by-AV-Pro-Designs)

Một phi công Mỹ đã nghỉ hưu có đam mê làm mô hình sân bay.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112510.webp)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112511.webp)

Website của ông có rất nhiều ảnh chụp các tác phẩm, bạn có thể nhấn vào xem.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112709.webp)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112710.webp)

Dưới đây là mô hình sân bay Mumbai, thậm chí còn có cả chế độ hiển thị cảnh đêm.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112512.webp)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112513.webp)

## Trích dẫn

1、[Nói không với những người đòi hỏi "một chút" thời gian của bạn](https://thoughtcatalog.com/ryan-holiday/2017/01/to-everyone-who-asks-for-just-a-little-of-your-time/)

Mọi người thường nói với tôi rằng:

> - Tôi muốn trò chuyện ngắn với anh một chút?
> - Tuần tới chúng ta đi uống cà phê nhé?
> - Chúng ta hãy cùng thảo luận một chút về việc này đi?

Câu trả lời của tôi luôn là: Không, không và không.

![](https://cdn.beekka.com/blogimg/asset/202408/bg2024082212.webp)

Tôi thực sự có thể đáp ứng yêu cầu của bạn, nhưng tôi chọn không làm thế.

Kể cả khi đó là cơ hội quan trọng, kể cả chỉ mất 15 phút, kể cả đó là việc mà ai cũng sẽ đồng ý, tôi vẫn không muốn làm.

Tôi phải giới hạn thời gian bị người khác chiếm dụng mỗi ngày, nếu không tôi sẽ chẳng còn thời gian cho chính mình.

Ngay cả khi tôi cho bạn mượn thời gian và vẫn còn thừa lại một ít, tôi vẫn có thể mất đi năng lượng và sự tập trung để sử dụng hiệu quả phần thời gian còn lại đó.

Thời gian là tài sản không thể thay thế nhất. Chúng ta không thể mua thêm thời gian. Chúng ta không thể lấy lại dù chỉ một giây đã mất. Chúng ta chỉ có thể hy vọng lãng phí nó ít nhất có thể.

Nhưng trong thực tế, không hiểu sao nhiều người lại coi thời gian là nguồn tài nguyên có khả năng tái tạo vô hạn nhất, dùng hết thì thôi, dù sao vẫn còn lúc khác.

![](https://cdn.beekka.com/blogimg/asset/202408/bg2024082213.webp)

Vì thế, nếu bạn hỏi tôi có thể trò chuyện hay gặp gỡ không, câu trả lời là không. Tôi hy vọng bạn hiểu lý do tôi trả lời như vậy.

## Ý kiến

1、

Lập trình là liều thuốc tốt nhất tôi từng gặp để kiềm chế sự ngạo mạn. Nếu ai đó quá ngạo mạn, hãy cứ để họ đi lập trình.

-- [tratt.net](https://tratt.net/laurie/blog/2020/automatic_syntax_error_recovery.html)

2、

Huấn luyện một mô hình có quan điểm khác biệt sẽ ngày càng khó khăn. Bởi vì nếu quan điểm của bạn không khớp với dữ liệu thực tế và thế giới thực, bạn không thể đơn giản dùng các tài liệu bên ngoài để dạy mô hình nữa.

-- [Độc giả Hacker News](https://news.ycombinator.com/item?id=46050177)

3、

Bây giờ là năm 2025, AI đang lan rộng như virus. Ngay cả khi bạn vẫn kiên trì làm ra những sản phẩm thủ công tinh xảo, mọi người vẫn dễ dàng nhầm lẫn công sức lao động của bạn với đống rác máy móc vô hồn và thiếu cảm hứng.

-- [tonsky.me](https://tonsky.me/blog/hiring-ai/)

4、

Đời người ngắn ngủi, cái chết đến thật nhẹ nhàng. Nếu tôi cứ để mình trôi theo dòng đời, chẳng mấy chốc tôi sẽ trở thành một lão già.

-- [Goro Obata](https://kottke.org/25/11/my-pace), một Youtuber Nhật Bản

5、

Nếu một vật dụng hữu dụng 100%, nó chắc chắn sẽ đẹp. Chẳng hạn không có chiếc đinh hay chiếc búa nào xấu xí cả. Tuy nhiên, có rất nhiều chiếc xe hơi xấu xí vì không phải mọi bộ phận của xe hơi đều hữu dụng.

-- [Dan Gelbart](https://www.bedelstein.com/post/mcmaster-carr), một nhà phát minh công nghiệp

(Hết)
