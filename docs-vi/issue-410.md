---
date: 2026-08-28
tags: ["ai", "trí tuệ nhân tạo", "mô hình ngôn ngữ", "llm", "lập trình", "công nghệ", "mã nguồn mở", "thuyết trình", "phần cứng", "phần mềm"]
---

# Ba cơ chế của AI mà bạn cần biết

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082701.webp)

Tác phẩm điêu khắc bịt mắt khổng lồ tại khu thắng cảnh Sa Pha Đầu, Ninh Hạ. ([via](https://www.4anet.com/p/01kzzn7qc04ts41frfk4zqjkc0))

## Ba cơ chế của AI mà bạn cần biết

Đây là bài viết thứ ba trong chuỗi "Kiến thức nhỏ về AI", hai bài trước lần lượt là [Mô hình lớn cần bao nhiêu bộ nhớ](https://www.ruanyifeng.com/blog/2026/07/weekly-issue-404.html) và [Cache trong AI là gì](https://www.ruanyifeng.com/blog/2026/08/weekly-issue-408.html).

Tôi muốn chia sẻ vài ghi chép học tập cá nhân để làm sáng tỏ cách hiểu về công nghệ AI. Tôi cố gắng diễn đạt thật giản dị, hy vọng sẽ hữu ích với mọi người.

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082703.webp)

Hôm nay chúng ta bàn về một câu hỏi cốt lõi: **Tại sao AI có thể trả lời câu hỏi của chúng ta, làm thế nào nó biết được đáp án?**

Bạn có thể tìm thấy vô số bài báo nghiên cứu và sách vở giải thích chi tiết cách thức vận hành của các mô hình ngôn ngữ lớn, nhưng chúng thường rất khó hiểu. Với người không chuyên, bạn chỉ cần nắm được [ba cơ chế cơ bản của AI](https://w4g1.dev/blog/models-are-getting-dumber-on-purpose) là đủ.

**(1) Cơ chế tham số**

Ở góc nhìn vĩ mô, **mọi mô hình lớn đều là nỗ lực mô hình hóa tri thức nhân loại**. Nó xây dựng một mô hình toán học nhằm mô tả toàn bộ kho tàng hiểu biết của con người.

Nó mô tả bằng cách nào? Mô hình dùng một cơ chế tham số để bóc tách tri thức thành từng đơn vị gọi là "token", rồi tính toán mối quan hệ toán học giữa tất cả các token với nhau. Quá trình này gọi là "huấn luyện" (training).

Mối quan hệ toán học đó được biểu diễn qua vô số tham số. Chẳng hạn, mô hình lớn GLM 5.3 có 744 tỷ tham số, những tham số này dùng để thiết lập mối liên kết giữa các token (chính là các trọng số). Bản chất của việc "huấn luyện" thực ra là tìm ra 744 tỷ trọng số đó để mô tả cấu trúc tri thức nhân loại, tức là mối tương quan giữa mọi token.

Khi quá trình huấn luyện hoàn tất, mỗi khi ta đặt câu hỏi, mô hình sẽ dựa vào các trọng số này để tìm ra token có khả năng xuất hiện cao nhất, từ đó tạo ra câu trả lời phù hợp nhất theo xác suất.

Vì vậy, **bản chất của mô hình lớn là một cơ chế "nén và tái tạo"**, nén tri thức con người vào vô số tham số, rồi sau đó giải nén tạo ra nội dung khi cần.

**(2) Cơ chế suy luận**

Dễ thấy rằng càng nhiều tham số thì mô hình hoạt động càng hiệu quả. Nhiều tham số hơn đồng nghĩa với việc mô tả tri thức chính xác hơn, và khả năng tái hiện thông tin cũng chuẩn xác hơn.

Dù vậy, một mặt chúng ta không thể tăng tham số vô hạn, vì chi phí huấn luyện lẫn chi phí vận hành sẽ tăng phi mã, thời gian tính toán khi xử lý cũng kéo dài.

Mặt khác, mô hình cũng không nhất thiết phải chứa đựng mọi kiến thức. Rất nhiều tri thức không cần lưu sẵn trong tham số, mà **hoàn toàn có thể suy ra qua suy luận logic**.

Chẳng hạn, chỉ cần biết tỷ lệ sinh và tỷ lệ tử của một thành phố, bạn lập tức tính được tỷ lệ tăng trưởng dân số tự nhiên. Bạn không cần phải ghi nhớ con số đó trong đầu, chỉ cần suy luận là ra.

Mô hình lớn cũng dựa vào cơ chế suy luận như vậy: từ những tri thức sẵn có trong tham số kết hợp với các quy tắc logic để suy ra những kiến thức mà nó chưa từng được nạp trực tiếp.

**(3) Cơ chế kết nối mạng**

Dù mô hình có sở hữu bao nhiêu tham số hay năng lực suy luận mạnh đến đâu, nó cũng không thể bao quát toàn bộ tri thức thế giới, luôn có những câu hỏi nó không thể tự trả lời.

Ví dụ, nếu bạn hỏi mô hình chỉ số đóng cửa của thị trường chứng khoán hôm nay là bao nhiêu, nó sẽ chịu thua. Tham số không lưu trữ dữ liệu thời gian thực này, và suy luận logic cũng không thể tính ra được.

Lúc này, mô hình phải dựa vào cơ chế kết nối mạng do Agent hoặc framework ứng dụng cung cấp, tự động truy cập internet để tìm kiếm những thông tin còn thiếu.

**(4) Tổng kết**

Chính nhờ sự kết hợp nhịp nhàng của ba cơ chế trên mà AI có thể trả lời thỏa đáng các câu hỏi của chúng ta.

Đầu tiên, cơ chế tham số cung cấp nền tảng tri thức cơ bản. Tiếp theo, cơ chế suy luận tạo ra tri thức mới thông qua lập luận logic. Cuối cùng, cơ chế kết nối mạng hỗ trợ thu thập những thông tin mà hai cơ chế trước không thể đáp ứng.

## Bí quyết thuyết trình trước đám đông

Nhiều người thường cảm thấy căng thẳng khi phải bước lên sân khấu và phát biểu trước đám đông.

Thực ra, chỉ cần nắm vững [vài bí quyết](https://blog.guillheu.dev/articles/first-time-speaker/) và định hình lại cách nhìn nhận, bạn hoàn toàn có thể thực hiện một bài thuyết trình thành công.

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082404.webp)

(1) Một bài thuyết trình thành công thì nội dung chỉ chiếm 30%, 70% còn lại nằm ở kỹ năng trình diễn.

Bạn cần hiểu rằng thuyết trình là một buổi biểu diễn. Bạn phải tận dụng triệt để giọng điệu, cử chỉ, biểu cảm và ngôn ngữ cơ thể để thu hút sự chú ý của khán giả. Nội dung thực chất không phải yếu tố mang tính quyết định tuyệt đối.

(2) Chuẩn bị thật kỹ lưỡng từ trước.

Bài phát biểu, slide, câu chuyện đùa, ngữ điệu, nhịp độ, tất cả chi tiết đều nên được luyện tập nhiều lần. Bạn không thể đoán trước điều gì sẽ xảy ra trên sân khấu, nhưng việc luyện tập kỹ càng giúp bạn luôn bám sát kịch bản đã định sẵn.

(3) Nếu bài nói liên quan đến chi tiết kỹ thuật, tốt nhất hãy tập trung nói về "lý do" (why), để khán giả hiểu vì sao họ nên quan tâm đến chủ đề này.

Còn về "cách làm" (how), bạn chỉ cần lướt qua ý tưởng khái quát và các khái niệm cơ bản. Hãy bỏ qua các bước triển khai chi tiết vì chẳng ai muốn nghe bạn đọc lại tài liệu hướng dẫn trên sân khấu.

(4) Căng thẳng là chuyện bình thường.

Thế nhưng, nếu bạn đã chuẩn bị kỹ càng và thuộc lòng nội dung, một khi đã nhập tâm vào bài nói, cảm giác hồi hộp sẽ nhanh chóng biến mất.

(5) Bất kể nói hay hay dở, bạn nhất định phải tự tin. Nếu chính bạn còn hoài nghi về điều mình đang nói, khán giả sẽ chẳng bao giờ bị thuyết phục.

Những người thuyết trình thành công luôn là những người tự tin, không hẳn là người giỏi nhất. Rất nhiều nhà quản lý vụng về hay thậm chí những kẻ lừa đảo vẫn có những bài phát biểu lôi cuốn, điều đó chứng minh chất lượng nội dung không phải điều kiện tiên quyết để bước lên bục diễn thuyết.

(6) Chỉ cần bạn thực sự khao khát chia sẻ về một chủ đề nào đó, bạn đã có đủ điều kiện để bước lên sân khấu.

## Tin tức công nghệ

1\. [Ghế phẳng](https://www.toxel.com/tech/2026/08/07/flat-chair-by-sara-paculdo/)

Một nhà thiết kế người Mỹ vừa sáng chế ra loại ghế bằng sợi thủy tinh mà khi nhận hàng, người dùng chỉ thấy một tấm phẳng duy nhất.

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082405.webp)

Chỉ mất vài phút để tháo rời các phần và ghép chúng lại thành một chiếc ghế hoàn chỉnh.

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082406.webp)

Thiết kế dạng tấm phẳng này giúp cắt giảm đáng kể thể tích vận chuyển, không gian lưu trữ và chi phí giao hàng.

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082407.webp)

Nó tận dụng độ căng của các đường cong cùng các khớp khóa cài vào nhau để tạo nên kết cấu chịu lực vô cùng chắc chắn.

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082408.webp)

2\. [Concert với đại diện ảo](https://www.billboard.com/music/country/dolly-parton-health-update-1236322526/)

Tuần này, nữ danh ca người Mỹ Dolly Parton đã qua đời ở tuổi 80. Tin tức này khiến công chúng ngỡ ngàng, bởi trước đó không lâu bà vừa thông báo chuẩn bị tổ chức một buổi hòa nhạc.

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082502.webp)

Thực chất, bà không trực tiếp lên sân khấu biểu diễn mà đã cấp quyền tạo một "hình đại diện ảo" (avatar) để biểu diễn thay mình.

Dù chưa tiết lộ nhiều chi tiết cụ thể, nhưng về mặt kỹ thuật, điều này hiện nay hoàn toàn khả thi. AI ngày nay không chỉ tái tạo giọng hát chân thực mà còn có thể render hình ảnh theo thời gian thực và tương tác với người hâm mộ.

Mô hình "concert avatar" mang lại rất nhiều lợi thế: có thể tổ chức liên tục nhiều suất diễn mỗi ngày, giá vé rẻ hơn, và thực hiện được những điều mà nghệ sĩ ngoài đời không thể làm, chẳng hạn như tổ chức concert cho những danh ca đã khuất. Rất có thể sau bước đi tiên phong này, thị trường sẽ chứng kiến một làn sóng bùng nổ của các buổi biểu diễn ảo.

3\. [Bộ trợ lực cho xe đạp](https://www.asus.com/accessories/bike-booster/asus-oxiis/oxiis-intelligent-bike-booster/)

ASUS vừa giới thiệu một bộ trợ lực xe đạp có thể lắp trên bất kỳ mẫu xe nào, biến chiếc xe đạp truyền thống thành xe đạp trợ lực điện trong nháy mắt.

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082704.webp)

Nguyên lý hoạt động khá đơn giản: một khối pin dẫn động trực tiếp một bánh lăn nhỏ.

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082705.webp)

Bạn chỉ cần gắn thiết bị lên phía trên bánh sau, bánh lăn sẽ ép vào lốp và truyền lực quay để đẩy xe về phía trước.

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082707.webp)

Thiết bị này cực kỳ hữu ích khi leo dốc hoặc chở hàng nặng, rất đáng để nhân rộng.

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082708.webp)

## Bài viết

1\. [Thời kỳ AI đầy biến động đã bắt đầu](https://www.gatesnotes.com/home/home-page-topic/reader/a-turbulent-ai-era-and-critical-choices-to-make) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082709.webp)

Bill Gates vừa đăng tải một bài viết trong tuần này, nhận định rằng AI tiềm ẩn nhiều rủi ro và chúng ta nên làm chậm lại tốc độ phát triển của nó.

Thế nhưng, vào năm 2023, chính ông từng chia sẻ một góc nhìn hoàn toàn trái ngược trong bài viết [Rủi ro của AI là có thật nhưng kiểm soát được](https://www.gatesnotes.com/work/make-ai-work-for-everyone/reader/the-risks-of-ai-are-real-but-manageable).

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082710.webp)

Điều gì đã khiến ông thay đổi quan điểm chỉ sau ba năm ngắn ngủi? Dù vậy, bất kể quan điểm cá nhân ra sao, đà tiến của AI lúc này chỉ có thể tăng tốc chứ không thể quay đầu chậm lại.

2\. [Ox Alpha chính là GLM](https://dejan.ai/blog/ox-alpha/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082504.webp)

Gần đây trên mạng xuất hiện một mô hình ẩn danh tên là Ox Alpha với hiệu năng vô cùng ấn tượng, khiến cộng đồng không ngừng đồn đoán về công ty đứng sau. Cuối cùng, Zhipu AI đã xác nhận đó chính là GLM 5.3 Flash.

Tuy nhiên, trước khi hãng chính thức công bố, đã có người tìm ra những bằng chứng thuyết phục chỉ ra tác giả đứng sau là Zhipu. Bài viết này chia sẻ phương pháp lần theo dấu vết để tìm ra đội ngũ phát triển mô hình.

Đáng chú ý, điểm Artificial Analysis của mô hình này đạt 57, cao hơn mức 53 của DeepSeek V4 Pro. Đây là một kết quả rất ấn tượng bởi số lượng tham số kích hoạt của nó chỉ có 18B, nhỏ hơn mức 49B của DeepSeek. Số lượng tham số tinh gọn giúp nó hoàn toàn có thể chạy mượt mà ngay trên máy tính cá nhân.

3\. [Hướng dẫn chi tiết sử dụng Git worktree](https://barrd.dev/article/parallel-development-without-the-headaches-using-git-worktree/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082402.webp)

Thông thường một kho chứa Git chỉ gắn với một thư mục làm việc, khiến việc chuyển đổi qua lại khi phát triển đồng thời hai hoặc ba tính năng trở nên khá bất tiện.

Lệnh git worktree cho phép bạn tạo nhiều thư mục làm việc song song từ cùng một repo, bài viết này giải thích chi tiết cách thiết lập và sử dụng.

4\. [Trang web AliExpress sử dụng WebAudio để nhận dạng thiết bị](https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082003.webp)

Một lập trình viên nước ngoài vô tình phát hiện trang chủ AliExpress có chứa đoạn mã khai thác WebAudio API, khiến tai nghe Bluetooth của anh bị ngắt kết nối mỗi khi mở trang. Sau khi kiểm tra mã nguồn, anh nhận ra đoạn mã này được dùng để lấy dấu vân tay (fingerprinting) nhận diện người dùng.

5\. [Lỗi xác thực tên miền trên Google Workspace](https://blog.elis.cc/articles/google-workspace-thinks-my-domain-is-an-email-provider/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082403.webp)

Dịch vụ văn phòng doanh nghiệp Google Workspace yêu cầu người dùng liên kết tên miền riêng, nhưng tên miền của tác giả liên tục bị hệ thống từ chối.

Tác giả liên hệ với đội ngũ hỗ trợ kỹ thuật nhưng chỉ nhận lại những phản hồi rập khuôn không giải quyết được vấn đề. Cuối cùng, anh tự kiểm tra mã nguồn frontend và phát hiện một hàm kiểm tra tên miền bị lỗi ở phía client. Chỉ cần vô hiệu hóa hàm này là tên miền được liên kết thành công. Thực trạng hỗ trợ kỹ thuật của Google hiện nay thực sự khiến nhiều người ngán ngẩm.

6\. [Tạo số ngẫu nhiên bằng thuật toán Xorshift](https://www.alanzucconi.com/2026/08/15/xorshift-generators/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082409.webp)

Có thể bạn chưa biết, phần lớn số ngẫu nhiên trong các tác vụ tính toán thường ngày được tạo ra bằng thuật toán Xorshift: thực hiện phép toán XOR và dịch bit liên tiếp trên giá trị seed. Bài viết đi sâu vào chi tiết triển khai cụ thể của giải thuật này.

## Công cụ

1\. [Vanilla OS 3](https://vanillaos.org)

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082601.webp)

Bản phân phối Linux dựa trên Debian, thiết kế theo hướng hệ thống bất biến (immutable), mọi thao tác cập nhật đều mang tính nguyên tử (atomic). (Đóng góp bởi [@NN708](https://github.com/ruanyf/weekly/issues/11356))

2\. [stock-tui](https://github.com/Folgerjun/stock-tui)

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082602.webp)

Công cụ dòng lệnh giúp theo dõi biểu đồ nến, tỷ số P/E và khối lượng giao dịch chứng khoán trực tiếp trong terminal. (Đóng góp bởi [@Folgerjun](https://github.com/ruanyf/weekly/issues/11354))

3\. [Dark mode PDFs](https://veil.simoneamico.com/)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032702.webp)

Trang web nhỏ thú vị giúp đảo ngược màu sắc file PDF tải lên, biến tài liệu nền trắng chữ đen thành nền đen chữ trắng để dễ đọc ban đêm.

4\. [Termio](https://github.com/termio-sh/termio)

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082410.webp)

Môi trường phát triển lập trình tích hợp AI (ADE) dành cho macOS, có phiên bản đồng bộ đi kèm trên iPhone. (Đóng góp bởi [@jiweiyuan](https://github.com/ruanyf/weekly/issues/11273))

5\. [PicLite](https://github.com/amiaoapp/PicLite)

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082411.webp)

Công cụ nén ảnh đa nền tảng, hỗ trợ theo dõi thư mục cục bộ, chuyển đổi định dạng ảnh, nén hàng loạt, gắn watermark và tự động tải lên dịch vụ lưu trữ ảnh. (Đóng góp bởi [@amiaoapp](https://github.com/ruanyf/weekly/issues/11290))

6\. [Multi-Row Tabs](https://github.com/hezhizheng/multi-row-tabs)

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082412.webp)

Tiện ích mở rộng cho Chrome giúp hiển thị toàn bộ các tab đang mở trong cửa sổ hiện tại dưới dạng nhiều dòng xếp lớp. (Đóng góp bởi [@hezhizheng](https://github.com/ruanyf/weekly/issues/11310))

7\. [InvoiceFlowAI](https://github.com/EthanYoQ/Invoice-Downloader)

Công cụ desktop mã nguồn mở hỗ trợ thu thập và thanh toán hóa đơn điện tử. Ứng dụng kết nối trực tiếp với hòm thư QQ hoặc 163 Mail của bạn để tải hóa đơn hàng loạt, nhận diện OCR, tự động phân loại lưu trữ và kết xuất báo cáo tổng hợp ra file Excel. (Đóng góp bởi [@EthanYoQ](https://github.com/ruanyf/weekly/issues/11327))

8\. [CozyClay](https://github.com/NomaDamas/CozyClay)

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082501.webp)

Công cụ trực quan hóa chạy trên trình duyệt cho phép bạn dựng khung bối cảnh, tạo dáng nhân vật, thiết lập chuyển động máy quay và biên tập cảnh quay, sau đó chuyển sang cho mô hình video AI để sinh video chuẩn xác hơn. (Đóng góp bởi [@HaD0Yun](https://github.com/ruanyf/weekly/issues/11329))

9\. [Email.md](https://www.emailmd.dev/templates)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032801.webp)

Trang web cung cấp các mẫu email định dạng sẵn, người dùng chỉ cần điền nội dung bằng cú pháp Markdown là hệ thống sẽ tự động tạo email chuẩn đẹp mắt.

10\. [Minimalytics](https://github.com/nafey/minimalytics)

![](https://cdn.beekka.com/blogimg/asset/202503/bg2025032101.webp)

Máy chủ phân tích thống kê nhỏ gọn để ghi nhận và theo dõi các loại sự kiện, viết bằng ngôn ngữ Go với cơ sở dữ liệu SQLite và tích hợp sẵn giao diện web quản trị.

## Tài nguyên

1\. [Căn cứ Starbase](https://www.spacex.com/sites/starbase-la)

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082603.webp)

SpaceX dự kiến xây dựng thêm một căn cứ Starbase mới tại bang Louisiana. Trang web giới thiệu dự án trông như bước ra từ một bộ phim khoa học viễn tưởng.

2\. [Dạo quanh San Francisco](https://sf.thijs.gg/)

![](https://cdn.beekka.com/blogimg/asset/202608/bg2026082503.webp)

Một tựa game trên nền web cho phép bạn tự do dạo bước khám phá đường phố San Francisco qua ảnh thực tế 360 độ hoặc chọn địa điểm tùy thích.

3\. [Bản đồ mạng lưới đường phố](https://anvaka.github.io/city-roads/) (city-roads)

![](https://cdn.beekka.com/blogimg/asset/202412/bg2024122612.webp)

Trang web trực quan hóa toàn bộ mạng lưới đường bộ của bất kỳ thành phố nào thành một bức vẽ đồ họa dạng đường nét (line art) tinh tế, có hỗ trợ thu phóng mượt mà.

## Hình ảnh

1\. [Những tác phẩm điêu khắc nhỏ nhất Luân Đôn](https://lookup.london/londons-smallest-public-sculptures/)

Thủ đô Luân Đôn sở hữu khá nhiều tác phẩm điêu khắc công cộng tí hon ẩn mình ở những nơi ít ai ngờ tới.

Trên góc cao tầng một của một con phố thương mại, có bức tượng hai chú chuột đang giằng nhau một miếng phô mai.

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051704.webp)

Tương truyền, bức tượng này được dựng lên để tưởng nhớ một câu chuyện bi kịch.

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051705.webp)

Vào thế kỷ 19, hai người thợ xây dựng tại đây đã ẩu đả kịch liệt vì một miếng phô mai bị thất lạc, dẫn đến án mạng thương tâm. Sau đó người ta mới phát hiện ra thủ phạm thực sự lấy cắp miếng phô mai chính là những chú chuột.

Ở một góc phố khác của Luân Đôn còn có bức điêu khắc "ngôi nhà chuột".

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051706.webp)

Chủ cửa hàng nhận thấy dãy số nhà trên phố bị khuyết mất một số, nên ông đã kỳ công tạo ra tác phẩm này để trao số nhà còn thiếu cho gia đình chuột.

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051707.webp)

Dưới đây là một số tác phẩm điêu khắc mini thú vị khác rải rác trong thành phố.

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051708.webp)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051709.webp)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051710.webp)

## Trích đoạn

1\. [Mạng lưới đồng nhất](https://www.science.org/doi/10.1126/science.aei2409)

Một đặc tính căn bản của mạng xã hội là chúng nuôi dưỡng các mạng lưới "đồng nhất" (homophilous networks).

Tính đồng nhất ở đây chỉ việc người dùng có xu hướng kết nối với những cá nhân có điểm tương đồng. Chẳng hạn, người thích ngắm chim sẽ tham gia hội nhóm ngắm chim trên mạng, người chơi bowling sẽ tụ họp cùng những người cùng sở thích.

Hệ quả là không gian mạng dễ dàng gom những nhóm người thiểu số hay dị biệt lại với nhau. Những người tin rằng Trái Đất phẳng có thể kết nối với nhau chỉ qua vài cú click, điều gần như bất khả thi trong đời thực vì số lượng người này quá ít ỏi và hiếm khi chạm mặt nhau ngoài phố.

Các mạng lưới đồng nhất này làm bóp méo nhận thức của con người về sự phân bổ các luồng quan điểm trong xã hội. Những người mang tư tưởng thiểu số, khi sống quá lâu trong "bong bóng" đồng nhất, thường ngộ nhận rằng quan điểm của mình đại diện cho tiếng nói của đại đa số. Hiện tượng này được gọi là hiệu ứng đồng thuận giả (false-consensus effect).

Hiệu ứng này kéo theo nhiều hệ lụy: Thứ nhất, nó củng cố niềm tin mù quáng vào các quan điểm dị biệt. Thứ hai, khi một người tin rằng quan điểm của mình được số đông ủng hộ, họ sẽ sinh ra bất mãn sâu sắc với các thể chế vận hành theo ý nguyện của đa số thực tế, từ đó nảy sinh cảm giác bị toàn xã hội cô lập và bài xích.

## Trích dẫn

1\.

Biểu hiện của một người có giáo dưỡng là khi họ có thể tận hưởng những điều tốt đẹp nhất, nhưng cũng sẵn sàng đón nhận và chịu đựng những điều tồi tệ nhất.

-- [Đường Sư Tăng](https://news.pku.edu.cn/xwzh/129-116805.htm), nhà báo nổi tiếng vừa qua đời trong tuần này

2\.

Thế giới chúng ta sống không phải lúc nào cũng là nơi mọi người biết đặt mình vào vị trí của người khác. Nhưng nếu bạn có thể giải thích thế giới cho một đứa trẻ 10 tuổi hiểu, hoặc thiết kế một chiếc nắp lọ mà một cụ già 80 tuổi cũng tự mở được, điều đó đôi khi sẽ giúp bạn hoàn thành mục tiêu ban đầu một cách trọn vẹn hơn rất nhiều.

-- [Hãy giải thích cho tôi như thể tôi là một đứa trẻ 10 tuổi](https://timharford.com/2026/08/explain-it-to-me-like-im-ten/)

3\.

Có người đã viết bài "Trực ca trực nhật đã là dĩ vãng", đề xuất nên để AI đảm nhận việc trực on-call. Chỉ khi AI không thể giải quyết được sự cố thì con người mới nên can thiệp, và chính AI sẽ là bên chủ động gọi người đến xử lý.

-- [Các sự cố về độ tin cậy liên quan đến AI đang ập đến](https://surfingcomplexity.blog/2026/08/22/wild-ai-related-reliability-incidents-are-coming/)

4\.

Mọi người dần nhận ra rằng việc dùng AI để học kiến thức mới diễn ra nhanh hơn nhiều so với các phương pháp truyền thống, bởi AI rất giỏi trong việc tổng hợp lượng lớn thông tin phân tán.

Tuy nhiên, khi học qua AI, bộ não không tham gia chủ động vào quá trình tiếp nhận, khiến mức độ hiểu sâu và ghi nhớ tri thức không bằng phương pháp học truyền thống. Bản chất hoạt động của não bộ con người cho thấy việc học lặp lại theo hình xoắn ốc là một trong những cách ghi nhớ kiến thức tốt nhất. AI cung cấp ngay kết quả cuối cùng, khiến chúng ta bỏ qua các bước chiêm nghiệm và trăn trở ở giữa.

-- [AI và kiểu tri thức của người tài xế](https://www.aaron-gray.com/ai-and-chauffeur-knowledge/)

5\.

Nếu giá nhà lao dốc, tài sản của tôi sẽ bị hao hụt, nhưng bù lại con cái tôi sẽ có cơ hội mua nhà với giá rẻ hơn. Đúng là phần tài sản thừa kế của chúng sẽ ít đi, nhưng chúng sẽ được hưởng mức chi phí nhà ở dễ chịu hơn trong suốt cả cuộc đời.

-- [Quy hoạch phát triển và hội chứng phản đối láng giềng (NIMBY)](https://www.betonit.ai/p/cds-vs-nimby)
