# Làn sóng mở API lần thứ hai

Bản tin này ghi lại những nội dung công nghệ đáng chia sẻ hàng tuần, phát hành vào thứ Sáu. (**[Thông báo] Nghỉ lễ Quốc tế Lao động vào thứ Sáu tuần tới, bản tin tạm nghỉ.**)

Tạp chí này [mã nguồn mở](https://github.com/ruanyf/weekly), hoan nghênh [đóng góp](https://github.com/ruanyf/weekly/issues). Ngoài ra còn có dịch vụ ["Ai đang tuyển dụng"](https://github.com/ruanyf/weekly/issues/9454), đăng tin tuyển dụng lập trình viên. Hợp tác vui lòng [liên hệ qua email](mailto:yifeng.ruan@gmail.com) (yifeng.ruan@gmail.com).

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042008.webp)

Biển quảng cáo ngầu nhất mà tôi từng thấy, chỉ có một dòng lệnh để quảng bá một bộ công cụ AI. Người bình thường không hiểu cũng chẳng sao, đằng nào nó cũng không dành cho họ. ([via](https://x.com/steventey/status/1689986179746197504))

## Làn sóng mở API lần thứ hai

Nếu bạn làm trong ngành Internet đủ lâu, chắc hẳn bạn sẽ nhớ rằng trước đây từng có một làn sóng mở API.

Đó là năm 2011, cách đây 15 năm, khi dịch vụ đám mây vừa mới trỗi dậy, các nền tảng đua nhau mở API của mình.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042102.webp)

Hồi đó, cả Facebook và Twitter đều phát hành API của mình và mở dữ liệu nền tảng. Thiết kế API của GitHub thậm chí còn là một tác phẩm nghệ thuật, gần như có thể lấy được bất kỳ tính năng nào bạn muốn.

Ý tưởng của các nền tảng lúc bấy giờ là việc mở API sẽ giúp người dùng và bên thứ ba tham gia phát triển các loại plugin và tiện ích mở rộng, từ đó thúc đẩy tăng trưởng cho nền tảng, tăng tỷ lệ giữ chân và sự hài lòng của người dùng.

Lúc đó còn có một trang web tên là [ProgrammableWeb](https://en.wikipedia.org/wiki/ProgrammableWeb) (hiện đã đóng cửa). Cái tên của nó đại diện cho niềm tin của mọi người thời bấy giờ: Internet có thể được lập trình thông qua API để kết nối dữ liệu của các nền tảng khác nhau lại với nhau.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042103.webp)

Thế nhưng, mọi chuyện đã diễn biến hoàn toàn ngược lại với dự đoán.

Các nền tảng nhận ra rằng API rất khó kiếm ra tiền vì không thể chèn quảng cáo, hơn nữa dữ liệu của chính mình lại giúp ích cho việc kinh doanh của công ty khác, gây thất thoát người dùng.

Thế là họ đua nhau thay đổi cách làm, hạn chế và đóng cửa API, không còn chia sẻ dữ liệu nữa, giữ người dùng trong "vườn rau có tường bao" của chính mình.

Ngày nay, API của Facebook và Twitter gần như chỉ để trưng cho đẹp, các ứng dụng bên thứ ba bị cấm triệt để. GitHub tuy vẫn giữ API mở nhưng cũng đã áp dụng kiểm soát, tăng cường xác thực danh tính và giới hạn tốc độ, khiến việc xây dựng các ứng dụng bên thứ ba đầy đủ tính năng trở nên rất khó khăn.

Đúng lúc mọi người nghĩ rằng đây sẽ là trạng thái bình thường thì một [sự thay đổi](https://brandur.org/second-wave-api-first) đã xuất hiện.

Vào nửa cuối năm 2025, các mô hình lớn đã đạt đến điểm tới hạn, trở nên thực sự mạnh mẽ và có thể sử dụng được cho môi trường sản xuất.

Mọi người nhanh chóng nhận ra rằng nếu mô hình lớn chỉ biết suy nghĩ mà không thể thực thi mã thì tác dụng sẽ không lớn. **Giá trị lớn nhất của AI không phải là tạo nội dung mà là tạo nội dung + tự động hóa**, như vậy mới có thể giải phóng sức lao động và tạo ra giá trị tối đa. Đại diện tiêu biểu cho tự động hóa AI tự thực thi mã chính là "Tôm hùm" (OpenClaw).

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042104.webp)

Tự động hóa có nghĩa là AI phải có khả năng gọi các nền tảng khác, và điều đó lại có nghĩa là các nền tảng khác trước tiên phải mở API của mình.

Bỗng chốc, API không còn là gánh nặng mà là điều kiện bắt buộc để kết nối với AI. Không có API, nền tảng của bạn sẽ không thể bước vào quy trình làm việc của AI, và các Agent khác nhau cũng không thể thay mặt người dùng làm việc trên nền tảng của bạn.

Cùng là hai nền tảng, một bên có API, bên kia không, thì bên không có API rất có thể sẽ bị thị trường bỏ rơi vì mô hình lớn không thể kết nối với nó, cũng không thể tự động hóa nó, và người dùng AI chỉ còn cách chuyển sang dùng đối thủ cạnh tranh của nó.

Các nền tảng đã nhận ra điều đó, ai mở API sớm thì người đó giành được tiên cơ. Cho nên, ngay cả một "ông lớn" như Tencent cũng mở giao diện WeChat với tốc độ nhanh nhất sau khi OpenClaw bùng nổ, để OpenClaw có thể gửi tin nhắn đến WeChat.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042315.webp)

Tencent cũng sợ rằng trong thế giới của OpenClaw sẽ không có chỗ cho mình. Các nền tảng khác lại càng không cần phải nói, tranh nhau mở giao diện thao tác của chính mình thông qua MCP và Skill.

Điều này cho thấy **làn sóng mở API lần thứ hai đang đến**. Lần này sẽ mở triệt để hơn và dễ sử dụng hơn lần trước.

(1) Lần này không chỉ mở các dịch vụ đám mây mà còn rất nhiều dịch vụ đời sống: giao đồ ăn, thương mại điện tử, ngân hàng... thậm chí còn có nhiều dịch vụ vốn dĩ không bao giờ có API như đặt chỗ nhà hàng và sân vận động.

(2) API lần này không cần lập trình thủ công, bạn chỉ cần sử dụng ngôn ngữ tự nhiên, được mô hình lớn dịch sang rồi gọi.

(3) API lần này là do người tiêu dùng gọi thông qua AI với mục đích là thay mặt người dùng thực hiện công việc. Trước đây API là do các ứng dụng gọi với mục đích lấy dữ liệu.

## Marathon robot

Cuối tuần trước, tại Diệc Trang, Bắc Kinh đã diễn ra [cuộc thi chạy bán marathon của robot hình người](https://news.sina.com.cn/zx/gj/2026-04-19/doc-inhvackq0239220.shtml) lần thứ hai.

Hơn 100 robot hình người đã tham gia cuộc thi để xem ai chạy hết quãng đường 21,0975 km nhanh nhất. Cuối cùng, thành tích của nhà vô địch là 50 phút 26 giây, vượt qua cả vận động viên con người nhanh nhất (kỷ lục thế giới bán marathon của con người là 1 giờ 02 phút 52 giây).

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042005.webp)

Theo [video hiện trường](https://x.com/xiaohu/status/2045786816213815411) do cư dân mạng quay lại, robot chạy được một khoảng cách nhất định phải vào trạm tiếp tế để nhân viên thay pin và thêm đá lạnh (hoặc đá khô) để tránh bị quá nhiệt.

Điều này có nghĩa là pin tích hợp của robot không duy trì nổi một giờ chạy.

Robot hình người [Unitree H2](https://www.unitree.com/cn/H2) được bán công khai có thời gian duy trì là 3 giờ. Khi vận động mạnh như chạy đường dài, thời gian duy trì chắc chắn sẽ bị giảm đi đáng kể. Hơn nữa, khi công suất như nhau, robot có trọng lượng nhẹ hơn sẽ có lợi thế trong cuộc đua, nghĩa là không thể mang theo quá nhiều pin.

Như vậy có thể thấy tính thực dụng của robot hình người hiện nay vẫn còn rất hạn chế. Khi không cắm điện, cứ sau một đến hai giờ là phải sạc, như thế thì rất nhiều việc sẽ không phù hợp để làm.

## GPT Images 2.0

Tuần này, OpenAI đã phát hành [mô hình GPT Image 2.0](https://openai.com/zh-Hans-CN/index/introducing-chatgpt-images-2-0/), được cho là mô hình hình ảnh mạnh nhất hiện nay, vượt qua cả Nano Banana 2 Pro của Google.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042304.webp)

Theo giới thiệu của OpenAI, việc hiển thị văn bản của nó có bước tiến lớn, hỗ trợ rất tốt chữ Hán và có thể tạo ra các hình ảnh giải thích phức tạp.

Mọi người có thể vào [ChatGPT.com](https://chatgpt.com/images) để dùng thử miễn phí.

Tôi đã làm một phép so sánh, tạo một bức ảnh chú chó nhỏ đang ngủ trưa dưới mái hiên của một trấn cổ. Đây là kết quả của GPT Images 1.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042306.webp)

Đây là kết quả của GPT Images 2.0.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042305.webp)

Tôi còn thấy một dự án thú vị là [Flipbook](https://flipbook.page/). Nó là một trình duyệt hình ảnh giải thích, người dùng nhập một chủ đề và nó sẽ tự động tạo ra hình ảnh giải thích chi tiết.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042307.webp)

Hình trên là hình ảnh giải thích được tạo ra khi nhập từ "nước ngọt", nhấp vào từng phần còn có thể tạo ra các lời giải thích sâu hơn.

Trên mạng đã có [kho lưu trữ Awesome](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) tập hợp các lời nhắc (prompt) ([@DophinL](https://github.com/ruanyf/weekly/issues/9728) đóng góp), mọi người có thể xem các ví dụ hay của người khác.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042308.webp)

Ngoài ra còn có một [kho lưu trữ lời nhắc](https://github.com/ZeroLu/awesome-gpt-image) tương tự ([@ZeroLu](https://github.com/ruanyf/weekly/issues/9727) đóng góp).

## AI là công cụ mở rộng thần kỳ

**AI có một đặc điểm là không chỉ có thể nén thông tin mà còn cực kỳ giỏi trong việc mở rộng thông tin**. Nó sẽ suy luận ra những phần mơ hồ và tạo ra những phần còn thiếu, lấp đầy các chi tiết có vẻ hợp lý.

Điều này có nghĩa là AI là công cụ mở rộng thần kỳ. [Có người](https://mattstromawn.com/writing/expansion-artifacts/) đã hình dung ra kịch bản thế này:

- CEO công ty khi họp đã nói miệng về một ý tưởng.
- AI mở rộng nó thành một tài liệu chiến lược.
- AI chuyển tài liệu chiến lược thành các thông số sản phẩm.
- AI sử dụng lập trình theo ngữ cảnh để tạo ra mã nguồn mẫu.
- AI dựa trên mã nguồn mẫu để viết thông cáo báo chí và bài PR.

Bạn thấy chưa, AI có thể biến một ý tưởng trong đầu thành tài liệu, mã nguồn, sản phẩm, buổi ra mắt, việc làm... liên tục được mở rộng ra.

Mọi người luôn nói rằng thế giới tương lai là một thế giới cực kỳ phong phú về sản phẩm vật chất, và AI có vẻ chính là loại công cụ đó: **Bất cứ thứ gì nó có thể tạo ra thì thứ đó sẽ trở nên cực kỳ phong phú**.

## Nhà vệ sinh trên xe hơi

Seres đã nộp đơn xin bằng sáng chế cho một chiếc "[nhà vệ sinh trên xe](https://chejiahao.autohome.com.cn/info/25229950)" dành cho xe hơi con.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042003.webp)

Ghế ngồi được lắp trên một đường ray, khi trượt về phía sau sẽ để lộ bồn cầu bên dưới.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042004.webp)

Bồn cầu này được trang bị bộ phận làm nóng dùng để làm bay hơi nước tiểu và sấy khô các chất bẩn khác, nhưng vẫn cần phải đổ thủ công định kỳ. Đồng thời xe cũng được trang bị quạt và ống xả dùng để thông gió.

Thiết bị này đối với xe hơi con thì bối cảnh sử dụng khá hạn chế, chỉ phù hợp khi gặp tắc đường kinh hoàng trên cao tốc. Thế nhưng đối với xe tải chạy đường dài thì nó lại rất thực dụng.

## Bài viết

1、[Đừng sử dụng Ollama](https://sleepingrobots.com/dreams/stop-using-ollama/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026041801.webp)

Ollama là một công cụ để chạy các mô hình lớn cục bộ. Bài viết này nêu ra rất nhiều vấn đề của nó và khuyên mọi người nên chuyển sang dùng [llama.cpp](https://github.com/ggml-org/llama.cpp) và [LM Studio](https://lmstudio.ai/).

2、[Các tính năng của npmx](https://nesbitt.io/2026/04/16/features-everyone-should-steal-from-npmx.html) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042202.webp)

Có người đã tạo ra một giao diện mới cho npmjs.com là [npmx.dev](https://npmx.dev/package/egg), giải quyết được rất nhiều tính năng mà các nhà phát triển yêu cầu bấy lâu nay.

3、[Đừng gọi chuỗi (method chaining) quá dài](https://allthingssmitty.com/2026/04/20/why-i-dont-chain-everything-in-javascript-anymore/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042313.webp)

Ngôn ngữ JavaScript có thể viết được những chuỗi gọi phương thức rất dài (hình trên), một số lập trình viên rất thích dùng. Bài viết này chỉ ra một số nhược điểm của việc gọi chuỗi và khuyên không nên dùng quá dài.

4、[Sự tiến hóa của kỹ thuật lập trình bất đồng bộ và thành quả thực tế](https://causality.blog/essays/what-async-promised/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042314.webp)

Một bài tổng quan giới thiệu nguồn gốc của lập trình bất đồng bộ, cách nó phát triển ra giải pháp async/await được chấp nhận rộng rãi hiện nay và những vấn đề tồn tại, được viết khá sâu sắc.

5、[Nguyên lý hoạt động của radar thụ động](https://www.passiveradar.com/how-passive-radar-works/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026041806.webp)

Radar có thể chủ động phát sóng điện từ để phát hiện vật thể bay, cũng có thể không phát sóng mà chỉ lắng nghe sự thay đổi của sóng điện từ, đó gọi là radar thụ động.

## Công cụ

1、[Little Snitch cho Linux](https://obdev.at/products/littlesnitch-linux/index.html)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026041812.webp)

Phần mềm giám sát truyền thông mạng nổi tiếng [Little Snitch](https://www.obdev.at/products/littlesnitch/index.html) cuối cùng cũng đã ra mắt phiên bản Linux. Bạn có thể dùng nó để xem mỗi ứng dụng đang kết nối với địa chỉ web nào.

2、[quien](https://github.com/retlehs/quien/)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026041807.webp)

Công cụ terminal để tra cứu thông tin tên miền với giao diện rõ ràng và dễ sử dụng.

3、[ggsql](https://ggsql.org/)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042101.webp)

Công cụ truy vấn SQL có thể tạo biểu đồ. Nó truy vấn trực tiếp vào cơ sở dữ liệu và biểu diễn kết quả dưới dạng biểu đồ trực quan, xem thêm [bài giới thiệu](https://opensource.posit.co/blog/2026-04-20_ggsql_alpha_release/).

4、[Himi Recorder](https://github.com/jrainlau/himi-recorder)

Ứng dụng quay màn hình cho Mac mã nguồn mở có thể vượt qua cơ chế phát hiện quay màn hình, khiến các ứng dụng bị quay không nhận biết được là đang bị quay màn hình. ([@jrainlau](https://github.com/ruanyf/weekly/issues/9663) đóng góp)

5、[Tab Harbor](https://github.com/V-IOLE-T/tab-harbor)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026041804.webp)

Tiện ích Chrome mã nguồn mở biến trang chủ của các tab mới mở thành trình quản lý tab. ([@V-IOLE-T](https://github.com/ruanyf/weekly/issues/9665) đóng góp)

Ngoài ra còn một tiện ích tương tự là [Tab Out](https://github.com/zarazhangrui/tab-out). ([@Acorn2](https://github.com/ruanyf/weekly/issues/9687) đóng góp)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042001.webp)

6、[animal-island-ui](https://github.com/guokaigdg/animal-island-ui)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026041805.webp)

Bộ thư viện thành phần React UI theo phong cách game "Animal Crossing". ([@guokaigdg](https://github.com/ruanyf/weekly/issues/9668) đóng góp)

7、[CUPS Web](https://github.com/hanxi/cups-web)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026041901.webp)

Công cụ quản lý máy in phiên bản web giúp điều khiển máy in từ xa qua trình duyệt, hỗ trợ nhiều người dùng và theo dõi lịch sử in ấn... ([@hanxi](https://github.com/ruanyf/weekly/issues/8587) đóng góp)

8、[Blog Helper](https://github.com/thinkycx/blog-helper)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026041902.webp)

Dịch vụ thống kê khách truy cập mã nguồn mở cung cấp thống kê PV/UV, bài viết hot, biểu đồ xu hướng... một phiên bản hỗ trợ được cho nhiều trang web. ([@thinkycx](https://github.com/ruanyf/weekly/issues/9677) đóng góp)

9、[HiKid](https://github.com/xiaochong/hi-kid)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042002.webp)

Ứng dụng desktop giúp trẻ em luyện nói và nghe tiếng Anh hoàn toàn miễn phí, hiện chỉ hỗ trợ macOS. ([@Hao4Wang](https://github.com/ruanyf/weekly/issues/9689) đóng góp)

10、[Kite Desktop](https://github.com/eryajf/kite-desktop)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042302.webp)

Công cụ quản lý đa cụm K8S phiên bản desktop. ([@eryajf](https://github.com/ruanyf/weekly/issues/9719) đóng góp)

11、[Project River](https://github.com/Lionad-Morotar/project-river)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042303.webp)

Biểu đồ hình con sông trực quan hóa lịch sử gửi mã của kho Git, hỗ trợ so sánh đa dự án, thông tin người đóng góp... [trải nghiệm trực tuyến](https://lionad-morotar.github.io/project-river). ([@Lionad-Morotar](https://github.com/ruanyf/weekly/issues/9722) đóng góp)

## AI

1、[OpenAI Privacy Filter](https://github.com/openai/privacy-filter)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042312.webp)

Làm sao để tránh gửi các thông tin nhạy cảm (như tên tuổi, địa chỉ, số điện thoại, mật khẩu) cho mô hình lớn?

OpenAI đã đưa ra câu trả lời: Privacy Filter. Đây là một mô hình lớn chạy cục bộ, nó sẽ xử lý trước rồi mới gửi cho mô hình lớn trực tuyến.

Ví dụ, văn bản gốc là "Ngày phát hành sản phẩm là 18/09/2026", sau khi xử lý sẽ thành "Ngày phát hành sản phẩm là [PRIVATE_DATE]", xem thêm tại [bài giới thiệu](https://openai.com/index/introducing-openai-privacy-filter/).

2、[LinkAI Gateway](https://github.com/ruanyf/weekly/issues/9657)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026041802.webp)

Cổng AI mã nguồn mở có thể kết nối với các mô hình lớn phổ biến, sau đó cung cấp API thống nhất (tương thích OpenAI) và bảng quản trị. ([@star7th](https://github.com/ruanyf/weekly/issues/9657) đóng góp)

3、[Nezha](https://github.com/hanshuaikang/nezha) (Na Tra)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042301.webp)

Trình quản lý nhiệm vụ lập trình AI mã nguồn mở giúp chuyển đổi nhanh chóng quản lý đa nhiệm, tích hợp các tính năng như terminal gốc, quản lý phiên làm việc, chỉnh sửa mã nguồn, Git... kích thước chưa đầy 10MB. ([@hanshuaikang](https://github.com/ruanyf/weekly/issues/9714) đóng góp)

4、[WatermarkZero](https://watermarkzero.org/)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026041803.webp)

Công cụ gỡ bỏ dấu chìm (watermark) nhìn thấy được của các hình ảnh do Gemini tạo ra. Hình ảnh không cần tải lên máy chủ mà được xử lý trực tiếp trên trình duyệt cục bộ. ([@liuyan-wjy](https://github.com/ruanyf/weekly/issues/9664) đóng góp)

5、[mini-cc](https://github.com/you-want/mini-cc)

AI Agent lập trình mã nguồn mở với tác dụng tương tự Claude Code, áp dụng kiến trúc đa ngôn ngữ, hiện đã hoàn thành triển khai phiên bản TypeScript. ([@RainyNight9](https://github.com/ruanyf/weekly/issues/9681) đóng góp)

## Tài nguyên

1、[The Listening Museum](https://sheets.works/data-viz/keyboard-sounds)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042006.webp)

Một trang web thú vị thu thập âm thanh gõ bàn phím. Bạn có thể nghe thử tiếng gõ của một loại bàn phím nào đó trước khi quyết định mua nó.

2、[Các định luật công nghệ phần mềm](https://lawsofsoftwareengineering.com/)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042201.webp)

Trang web này thu thập các định luật liên quan đến phần mềm, hiện có 56 điều.

Ví dụ, "[Định luật Parkinson](https://lawsofsoftwareengineering.com/laws/parkinsons-law/)" (Parkinson's Law): Khối lượng công việc luôn tăng lên cho đến khi lấp đầy mọi khoảng thời gian trống khả dụng. Hệ quả là dù bạn thiết lập thời gian phát triển dài bao nhiêu thì dự án cũng sẽ luôn làm đến tận phút cuối cùng.

## Hình ảnh

1、[Font chữ tiếng Anh 5x5 pixel](https://maurycyz.com/projects/mcufont/)

Font chữ tiếng Anh nhỏ nhất là bao nhiêu?

1x1 pixel (rộng 1, cao 1) chỉ là một dấu chấm, tất nhiên là không thể. 2x2 pixel cũng không thể. 3x3 pixel về lý thuyết là được nhưng thực tế không thể đọc được. 4x4 pixel thì khó vẽ được một số ký tự nhiều nét như E, M, W.

Vì vậy, font chữ tiếng Anh nhỏ nhất chính là 5x5 pixel, kết quả như dưới đây.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042309.webp)

Trong font chữ trên, hầu hết các chữ thường nhỏ hơn chữ hoa một pixel để có thể phân biệt được bằng mắt thường.

Toàn bộ font chữ chỉ chiếm 350 byte bộ nhớ, vì vậy nó rất phù hợp cho các thiết bị cũ hoặc thiết bị cấu hình thấp, ngay cả bộ vi điều khiển 8-bit chỉ có 16kB bộ nhớ cũng có thể hoàn thành việc nạp font.

Ngoài ra mỗi ký tự của nó chỉ cần 25 pixel để hiển thị, mà ngay cả màn hình 384x288 cũng đã có 110.000 pixel.

Ngoài font 5x5 còn có font 3x5 (rộng 3, cao 5) và font 4x5 (rộng 4, cao 5) nhưng hiệu quả nhận diện của chúng đều không tốt (hình dưới).

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042310.webp)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042311.webp)

2、[Thành phố dầu khí trên biển Caspi](https://www.cnn.com/2024/11/06/climate/oil-rocks-neft-daslari-caspian-sea-city/index.html)

Biển Caspi là hồ nước lớn nhất thế giới với diện tích tương đương tỉnh Vân Nam.

Vào giữa thế kỷ trước, Caspi phát hiện ra dầu mỏ. Khi đó Liên Xô đã bắt đầu xây dựng các giàn khoan trên mặt hồ, cách bờ biển 60 dặm, phải mất 6 tiếng đi phà mới tới nơi.

Lúc cao điểm nhất có tổng cộng khoảng 320 cơ sở sản xuất bao gồm 2.000 giếng dầu được kết nối với nhau bởi hơn 100 dặm cầu dẫn.

![](https://cdn.beekka.com/blogimg/asset/202411/bg2024111007.webp)

Thời đó có hơn 5.000 người sinh sống trên các giàn khoan này, tạo thành một thành phố trên mặt nước khó tin với tất cả các tòa nhà chung cư đều được xây trên mặt nước.

![](https://cdn.beekka.com/blogimg/asset/202411/bg2024111008.webp)

Cùng với sự cạn kiệt của các mỏ dầu và sự biến động của giá dầu, sản lượng của thành phố dầu khí này đã sụt giảm mạnh, mọi người hầu như đã rời đi, toàn bộ các giàn khoan đều trong tình trạng xuống cấp và việc sụp đổ chỉ là vấn đề thời gian.

![](https://cdn.beekka.com/blogimg/asset/202411/bg2024111009.webp)

## Trích dẫn

1、

Nhà sản xuất giày Allbirds của Mỹ tuyên bố chuyển đổi thành công ty AI, giá cổ phiếu đã tăng vọt 5 lần trong một ngày.

Điều này làm gợi nhớ đến năm 2017, một doanh nghiệp nước giải khát của Mỹ tên là "Trà đá Long Island" đã tuyên bố chuyển đổi thành công ty blockchain, vừa bán trà chanh vừa tìm kiếm cơ hội đầu tư blockchain, giá cổ phiếu cũng tăng vọt. Sau đó mảng kinh doanh blockchain chưa kịp thiết lập thì nó đã phá sản.

-- [Yahoo](https://gemini.google.com/app/1833a525ff94d60a)

2、

Figma sở hữu gần 2.000 nhân viên (tất nhiên không phải tất cả đều làm phát triển sản phẩm), trong khi tôi nghi ngờ liệu đội ngũ phát triển Claude Design mới ra mắt của Anthropic có vượt quá 10 người hay không.

-- [《Thế bí của Figma》](https://finance.yahoo.com/quote/FIG/), bài viết này nhận định Claude Design sẽ giáng một đòn mạnh vào Figma, trước tốc độ và chi phí phát triển của AI thì các phần mềm truyền thống trở nên yếu thế.

3、

Viễn cảnh về thế giới tương lai trong tôi là nó có lẽ không tràn đầy cảm giác tương lai đến thế, mà ngược lại giống như một bài thơ đồng quê. Chúng ta có thể quay lại hình thái sinh hoạt truyền thống mà vẫn không từ bỏ sự tiện lợi do công nghệ mới mang lại, hầu như không cần phải nhìn hay chạm vào màn hình nữa.

-- [jsomers.net](https://jsomers.net/blog/the-paper-computer)

4、

Mỗi một nền văn hóa đều sẽ tạo ra những anh hùng phản ánh nỗi lo âu sâu sắc nhất của họ.

Điều mà Thung lũng Silicon lo lắng nhất chính là sự đình trệ tăng trưởng, không thể tạo ra những sản phẩm mới được thị trường đón nhận nồng nhiệt. Thế nên họ ra sức quảng bá về những "anh hùng lập trình": những người có thể phát hành tính năng mới vào lúc nửa đêm, dựa vào ý chí mạnh mẽ do caffeine mang lại để biến những nét vẽ trên bảng trắng thành những doanh nghiệp kỳ lân trị giá hàng chục tỷ USD.

-- [《Bài ca của những người duy trì cổ điển》](https://www.joanwestenberg.com/the-rime-of-the-ancient-maintainer/)

## Nhìn lại các năm trước

[Cách phá giải khởi động lạnh](https://www.ruanyifeng.com/blog/2025/05/weekly-issue-347.html)（#347）

[Đồ chơi chim uống nước](https://www.ruanyifeng.com/blog/2024/04/weekly-issue-297.html)（#297）

[Thư sa thải của Zuckerberg](https://www.ruanyifeng.com/blog/2023/03/weekly-issue-247.html)（#247）

[Nếu thế giới này có chiếc máy hạnh phúc](https://www.ruanyifeng.com/blog/2022/03/weekly-issue-197.html)（#197）

(Hết)
