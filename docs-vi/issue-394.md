---
tags: [API, Open Source, Mã nguồn mở, Technology, Công nghệ, Web Development, Phát triển Web, Programming, Lập trình, Internet]
---

# Làn sóng mở API lần thứ hai

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042008.webp)

Đây là tấm biển quảng cáo ngầu nhất mà tôi từng thấy. Chỉ vỏn vẹn một dòng lệnh để quảng bá một bộ công cụ AI. Người bình thường không hiểu cũng chẳng sao, vốn dĩ nó cũng không dành cho họ. ([via](https://x.com/steventey/status/1689986179746197504))

## Làn sóng mở API lần thứ hai

Nếu bạn làm trong ngành Internet đủ lâu, chắc hẳn bạn vẫn còn nhớ về làn sóng mở API thuở trước.

Đó là năm 2011, cách đây đúng 15 năm. Khi đó dịch vụ đám mây mới chớm nở, các nền tảng đua nhau mở API.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042102.webp)

Hồi ấy, cả Facebook lẫn Twitter đều tung ra API và mở toang dữ liệu nền tảng. Thiết kế API của GitHub khi đó thực sự là một tác phẩm nghệ thuật, bạn gần như có thể lấy bất kỳ tính năng nào mình muốn.

Ý tưởng của các ông lớn lúc bấy giờ rất rõ ràng: mở API để lôi kéo người dùng và bên thứ ba cùng phát triển plugin, tiện ích. Từ đó thúc đẩy tăng trưởng, giữ chân người dùng và khiến họ hài lòng hơn.

Ngày đó còn có một trang web tên là [ProgrammableWeb](https://en.wikipedia.org/wiki/ProgrammableWeb) (giờ đã đóng cửa). Cái tên này đại diện cho niềm tin mãnh liệt của giới công nghệ thời bấy giờ: Chúng ta có thể lập trình Internet thông qua API để kết nối dữ liệu giữa các nền tảng khác nhau.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042103.webp)

Thế nhưng, thực tế lại đi ngược hoàn toàn với kỳ vọng.

Các nền tảng nhận ra rằng API rất khó kiếm ra tiền vì không thể chèn quảng cáo. Chưa kể, dữ liệu của chính mình lại đang làm giàu cho công ty khác và khiến người dùng rời bỏ hệ sinh thái.

Vậy là họ đồng loạt quay xe. Họ hạn chế, đóng cửa API, ngừng chia sẻ dữ liệu và nhốt người dùng trong những "vườn rau có tường bao" của riêng mình.

Đến nay, API của Facebook và Twitter gần như chỉ để làm cảnh. Các ứng dụng bên thứ ba bị khai tử không thương tiếc. GitHub tuy vẫn giữ API mở nhưng cũng siết chặt quản lý, tăng cường xác thực và giới hạn tốc độ. Việc xây dựng một ứng dụng bên thứ ba đầy đủ tính năng giờ đây khó như lên trời.

Đúng lúc mọi người nghĩ rằng đây sẽ là trạng thái bình thường mới thì một [sự thay đổi](https://brandur.org/second-wave-api-first) đã xuất hiện.

Vào nửa cuối năm 2025, các mô hình lớn đã đạt đến điểm tới hạn. Chúng trở nên thực sự mạnh mẽ và sẵn sàng cho môi trường thực tế.

Chúng ta nhanh chóng nhận ra một điều: nếu mô hình lớn chỉ biết suy nghĩ mà không thể thực thi mã, giá trị của nó sẽ cực kỳ hạn chế. **Giá trị lớn nhất của AI không nằm ở việc tạo nội dung, mà là tạo nội dung cộng với tự động hóa**. Chỉ có như vậy mới thực sự giải phóng sức lao động và tạo ra giá trị tối đa. Đại diện tiêu biểu cho xu hướng AI tự chạy code chính là "OpenClaw".

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042104.webp)

Tự động hóa đồng nghĩa với việc AI phải có khả năng gọi các nền tảng khác. Và để làm được điều đó, các nền tảng bắt buộc phải mở API của mình.

Bỗng chốc, API không còn là gánh nặng mà trở thành điều kiện tiên quyết để kết nối với thế giới AI. Thiếu API, nền tảng của bạn sẽ bị gạt ra khỏi quy trình làm việc của AI. Các Agent sẽ không thể thay mặt người dùng làm việc trên hệ thống của bạn.

Hãy tưởng tượng hai nền tảng cạnh tranh, một bên có API, bên kia không. Bên không có API rất dễ bị thị trường đào thải vì các mô hình lớn không thể kết nối hay tự động hóa nó. Người dùng AI đương nhiên sẽ chọn đối thủ của bạn.

Các ông lớn đã nhận ra điều này. Ai mở API sớm, người đó chiếm ưu thế. Ngay cả một đế chế như Tencent cũng phải vội vã mở giao diện WeChat sau khi OpenClaw bùng nổ, để nó có thể gửi tin nhắn trực tiếp qua WeChat.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042315.webp)

Tencent cũng sợ rằng trong thế giới AI sẽ không có chỗ cho mình. Các nền tảng khác lại càng sốt sắng hơn, tranh nhau mở giao diện thao tác thông qua MCP và Skill.

Tất cả những điều này cho thấy **làn sóng mở API lần thứ hai đang ập đến**. Lần này sẽ triệt để hơn và dễ dùng hơn nhiều.

(1) Phạm vi mở rộng không chỉ ở các dịch vụ đám mây mà còn len lỏi vào mọi ngóc ngách đời sống: giao đồ ăn, thương mại điện tử, ngân hàng... Thậm chí cả những nơi vốn chẳng bao giờ nghĩ đến API như đặt chỗ nhà hàng hay sân bóng.

(2) API giờ đây không cần lập trình thủ công phức tạp. Bạn chỉ cần dùng ngôn ngữ tự nhiên, mô hình lớn sẽ tự dịch và thực hiện lệnh gọi.

(3) API lần này do người tiêu dùng gọi thông qua AI, với mục đích thay mặt họ thực thi công việc. Khác hẳn với trước đây, khi API chủ yếu để các ứng dụng lấy dữ liệu.

## Marathon robot

Cuối tuần trước tại Diệc Trang, Bắc Kinh, [cuộc thi chạy bán marathon dành cho robot hình người](https://news.sina.com.cn/zx/gj/2026-04-19/doc-inhvackq0239220.shtml) lần thứ hai đã diễn ra.

Hơn 100 robot đã cùng so tài trên quãng đường 21,0975 km. Kết quả thật kinh ngạc: nhà vô địch cán đích với thời gian 50 phút 26 giây, vượt xa kỷ lục thế giới của con người (1 giờ 02 phút 52 giây).

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042005.webp)

Theo [video tại hiện trường](https://x.com/xiaohu/status/2045786816213815411), robot chạy được một quãng là phải vào trạm tiếp tế để nhân viên thay pin và thêm đá lạnh để hạ nhiệt.

Điều này cho thấy pin tích hợp của robot chưa trụ nổi một giờ chạy cường độ cao. Dòng robot [H2 của Unitree](https://www.unitree.com/cn/H2) có thời lượng pin 3 giờ ở điều kiện thường, nhưng khi chạy marathon thì tiêu tốn năng lượng hơn nhiều. Ngoài ra, robot cần nhẹ để chạy nhanh, nghĩa là không thể mang quá nhiều pin.

Có thể thấy tính thực dụng của robot hình người hiện nay vẫn còn hạn chế. Nếu không cắm điện mà cứ chạy một hai giờ lại phải sạc thì rõ ràng chúng chưa thể đảm đương được nhiều công việc thực tế.

## GPT Images 2.0

Tuần này, OpenAI đã tung ra [mô hình GPT Image 2.0](https://openai.com/zh-Hans-CN/index/introducing-chatgpt-images-2-0/). Đây được coi là mô hình hình ảnh mạnh nhất hiện nay, vượt mặt cả Nano Banana 2 Pro của Google.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042304.webp)

Theo OpenAI, khả năng render văn bản của nó đã tiến bộ vượt bậc, hỗ trợ chữ Hán cực tốt và có thể tạo ra các hình ảnh giải thích phức tạp. Bạn có thể trải nghiệm miễn phí tại [ChatGPT.com](https://chatgpt.com/images).

Tôi đã thử làm một phép so sánh nhỏ: yêu cầu tạo hình một chú chó đang ngủ trưa dưới mái hiên của một trấn cổ. Đây là kết quả từ GPT Images 1.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042306.webp)

Và đây là GPT Images 2.0.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042305.webp)

Tôi còn tìm thấy một dự án khá hay là [Flipbook](https://flipbook.page/). Đây là một trình duyệt hình ảnh giải thích. Người dùng chỉ cần nhập chủ đề, hệ thống sẽ tự động tạo ra các hình ảnh minh họa chi tiết.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042307.webp)

Hình trên là kết quả khi tôi nhập từ khóa "nước ngọt". Bạn có thể click vào từng phần để xem giải thích sâu hơn.

Cộng đồng cũng đã nhanh tay tổng hợp các Prompt xịn tại [kho lưu trữ Awesome](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) (do bạn [@DophinL](https://github.com/ruanyf/weekly/issues/9728) gửi về).

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042308.webp)

Ngoài ra còn một [kho lưu trữ Prompt khác](https://github.com/ZeroLu/awesome-gpt-image) tương tự (do bạn [@ZeroLu](https://github.com/ruanyf/weekly/issues/9727) đóng góp).

## AI là cỗ máy khuếch đại

**AI có một đặc điểm thú vị: nó không chỉ biết nén thông tin mà còn cực kỳ giỏi trong việc mở rộng chúng**. Nó có thể tự suy luận ra những phần mơ hồ, thậm chí tạo ra những mẩu thông tin còn thiếu để lấp đầy các chi tiết một cách hợp lý.

Điều này biến AI thành một công cụ khuếch đại quyền năng. [Có người](https://mattstromawn.com/writing/expansion-artifacts/) đã hình dung ra kịch bản thế này:

- CEO chỉ cần nói ra một ý tưởng trong cuộc họp.
- AI sẽ triển khai nó thành một bản kế hoạch chiến lược.
- Từ đó, AI tiếp tục cụ thể hóa thành các thông số kỹ thuật sản phẩm.
- Rồi AI tự chạy code để tạo ra bản mẫu (prototype).
- Cuối cùng, AI soạn luôn thông cáo báo chí cho sản phẩm đó.

Bạn thấy đấy, AI có thể biến một ý tưởng trong đầu thành tài liệu, code, sản phẩm, và cả chiến dịch truyền thông. Chúng ta thường nói về một tương lai vật chất dư thừa. AI chính là công cụ đưa chúng ta đến đó: **Bất cứ thứ gì nó có thể tạo ra, thứ đó sẽ trở nên cực kỳ phong phú.**

## Toilet trên xe hơi

Hãng xe Seres vừa đăng ký bằng sáng chế cho một chiếc "[toilet trên xe hơi](https://chejiahao.autohome.com.cn/info/25229950)".

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042003.webp)

Phần ghế ngồi được đặt trên một đường ray. Khi trượt ghế ra phía sau, chiếc bồn cầu bên dưới sẽ lộ ra.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042004.webp)

Hệ thống này có bộ phận gia nhiệt để làm bay hơi nước tiểu và sấy khô chất thải, dù thỉnh thoảng bạn vẫn phải đi đổ thủ công. Xe cũng được trang bị quạt và ống xả riêng để thông gió. Tiện ích này trên xe con hơi thừa thãi, có lẽ chỉ phát huy tác dụng khi tắc đường nghiêm trọng. Nhưng với những bác tài chạy xe tải đường dài, đây chắc chắn là một cứu cánh tuyệt vời.

## Bài viết hay

1、[Đừng dùng Ollama nữa](https://sleepingrobots.com/dreams/stop-using-ollama/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026041801.webp)

Ollama là một công cụ chạy mô hình lớn tại chỗ rất phổ biến. Tuy nhiên, tác giả bài viết này chỉ ra khá nhiều vấn đề của nó và khuyên chúng ta nên chuyển sang dùng [llama.cpp](https://github.com/ggml-org/llama.cpp) hoặc [LM Studio](https://lmstudio.ai/).

2、[Những tính năng đáng học hỏi từ npmx](https://nesbitt.io/2026/04/16/features-everyone-should-steal-from-npmx.html) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042202.webp)

Có người đã xây dựng một giao diện mới cho npmjs.com mang tên [npmx.dev](https://npmx.dev/package/egg), giải quyết được rất nhiều vấn đề mà giới lập trình hằng mong mỏi.

3、[Đừng lạm dụng Chain Call quá dài](https://allthingssmitty.com/2026/04/20/why-i-dont-chain-everything-in-javascript-anymore/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042313.webp)

JavaScript cho phép viết những chuỗi gọi hàm (chaining) rất dài. Bài viết này cảnh báo về những mặt trái của nó khi chuỗi lệnh trở nên quá rắc rối.

4、[Sự tiến hóa của lập trình bất đồng bộ](https://causality.blog/essays/what-async-promised/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042314.webp)

Một bài tổng hợp sâu sắc về nguồn gốc của lập trình bất đồng bộ, cách mà async/await trở thành chuẩn mực, và cả những vấn đề còn tồn tại.

5、[Radar thụ động hoạt động thế nào?](https://www.passiveradar.com/how-passive-radar-works/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026041806.webp)

Thông thường radar sẽ chủ động phát sóng điện từ để dò tìm vật thể. Nhưng radar thụ động thì không phát gì cả, nó chỉ lặng lẽ "nghe" sự thay đổi của các sóng điện từ xung quanh.

## Công cụ

1、[Little Snitch cho Linux](https://obdev.at/products/littlesnitch-linux/index.html)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026041812.webp)

Phần mềm giám sát mạng nổi tiếng trên Mac cuối cùng cũng đã có phiên bản cho Linux. Bạn có thể theo dõi xem từng ứng dụng đang kết nối đi đâu.

2、[quien](https://github.com/retlehs/quien/)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026041807.webp)

Công cụ dòng lệnh để tra cứu thông tin tên miền với giao diện trực quan.

3、[ggsql](https://ggsql.org/)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042101.webp)

Công cụ truy vấn SQL có khả năng vẽ biểu đồ trực tiếp từ database.

4、[Himi Recorder](https://github.com/jrainlau/himi-recorder)

Ứng dụng quay màn hình mã nguồn mở cho Mac, có thể lách qua các cơ chế phát hiện quay màn hình của các ứng dụng khác. ([@jrainlau](https://github.com/ruanyf/weekly/issues/9663) đóng góp)

5、[Tab Harbor](https://github.com/V-IOLE-T/tab-harbor)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026041804.webp)

Extension mã nguồn mở cho Chrome giúp biến trang tab mới thành một trình quản lý tab xịn xò. ([@V-IOLE-T](https://github.com/ruanyf/weekly/issues/9665) đóng góp)

Dự án tương tự là [Tab Out](https://github.com/zarazhangrui/tab-out). ([@Acorn2](https://github.com/ruanyf/weekly/issues/9687) đóng góp)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042001.webp)

6、[animal-island-ui](https://github.com/guokaigdg/animal-island-ui)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026041805.webp)

Bộ UI component cho React mang phong cách của tựa game *Animal Crossing*. ([@guokaigdg](https://github.com/ruanyf/weekly/issues/9668) đóng góp)

7、[CUPS Web](https://github.com/hanxi/cups-web)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026041901.webp)

Công cụ quản lý máy in qua giao diện web, cho phép điều khiển từ xa và theo dõi lịch sử in ấn. ([@hanxi](https://github.com/ruanyf/weekly/issues/8587) đóng góp)

8、[Blog Helper](https://github.com/thinkycx/blog-helper)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026041902.webp)

Dịch vụ thống kê lượt truy cập mã nguồn mở, cung cấp các chỉ số PV/UV, bài viết hot và biểu đồ xu hướng. ([@thinkycx](https://github.com/ruanyf/weekly/issues/9677) đóng góp)

9、[HiKid](https://github.com/xiaochong/hi-kid)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042002.webp)

Ứng dụng desktop giúp trẻ em luyện nghe nói tiếng Anh hoàn toàn miễn phí (chỉ hỗ trợ macOS). ([@Hao4Wang](https://github.com/ruanyf/weekly/issues/9689) đóng góp)

10、[Kite Desktop](https://github.com/eryajf/kite-desktop)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042302.webp)

Công cụ quản lý đa cluster K8S ngay trên desktop. ([@eryajf](https://github.com/ruanyf/weekly/issues/9719) đóng góp)

11、[Project River](https://github.com/Lionad-Morotar/project-river)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042303.webp)

Hình ảnh hóa lịch sử commit của Git dưới dạng dòng sông. ([@Lionad-Morotar](https://github.com/ruanyf/weekly/issues/9722) đóng góp)

## AI liên quan

1、[OpenAI Privacy Filter](https://github.com/openai/privacy-filter)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042312.webp)

Làm sao để không bị lộ thông tin nhạy cảm khi gửi Prompt cho AI? OpenAI vừa tung ra Privacy Filter. Đây là một mô hình chạy cục bộ để lọc dữ liệu trước khi gửi lên mây.

2、[LinkAI Gateway](https://github.com/ruanyf/weekly/issues/9657)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026041802.webp)

AI Gateway mã nguồn mở, cho phép kết nối với nhiều mô hình khác nhau và cung cấp một API thống nhất. ([@star7th](https://github.com/ruanyf/weekly/issues/9657) đóng góp)

3、[Nezha](https://github.com/hanshuaikang/nezha) (Na Tra)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042301.webp)

Trình quản lý nhiệm vụ lập trình bằng AI, tích hợp sẵn terminal, trình soạn thảo mã và Git. ([@hanshuaikang](https://github.com/ruanyf/weekly/issues/9714) đóng góp)

4、[WatermarkZero](https://watermarkzero.org/)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026041803.webp)

Công cụ xóa hình mờ trên ảnh do Gemini tạo ra, xử lý trực tiếp trên trình duyệt. ([@liuyan-wjy](https://github.com/ruanyf/weekly/issues/9664) đóng góp)

5、[mini-cc](https://github.com/you-want/mini-cc)

Một AI Agent hỗ trợ lập trình tương tự như Claude Code, hiện đã triển khai bằng TypeScript. ([@RainyNight9](https://github.com/ruanyf/weekly/issues/9681) đóng góp)

## Tài nguyên

1、[The Listening Museum](https://sheets.works/data-viz/keyboard-sounds)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042006.webp)

Trang web sưu tầm âm thanh gõ phím. Bạn có thể vào đây nghe thử tiếng của từng loại bàn phím trước khi mua.

2、[Các định luật kỹ nghệ phần mềm](https://lawsofsoftwareengineering.com/)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042201.webp)

Nơi tổng hợp các quy luật trong ngành phần mềm. Ví dụ như "Định luật Parkinson": Công việc luôn tự phình to ra để lấp đầy khoảng thời gian mà bạn dành cho nó.

## Hình ảnh

1、[Font chữ 5x5 pixel](https://maurycyz.com/projects/mcufont/)

Kích thước tối thiểu của một font chữ tiếng Anh là bao nhiêu? Câu trả lời là 5x5 pixel. Nhỏ hơn mức này, chúng ta hầu như không thể phân biệt được các chữ cái phức tạp.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042309.webp)

Font chữ này cực nhẹ, chỉ chiếm 350 byte bộ nhớ, cực kỳ phù hợp cho các thiết bị đời cũ hoặc vi điều khiển cấp thấp.

Ngoài ra còn có các font 3x5 và 4x5 nhưng độ nhận diện kém hơn nhiều (hình dưới).

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042310.webp)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042311.webp)

2、[Thành phố dầu khí trên biển Caspi](https://www.cnn.com/2024/11/06/climate/oil-rocks-neft-daslari-caspian-sea-city/index.html)

Vào giữa thế kỷ trước, Liên Xô đã xây dựng một hệ thống giàn khoan khổng lồ trên mặt hồ Caspi.

![](https://cdn.beekka.com/blogimg/asset/202411/bg2024111007.webp)

Tại đây từng có 5000 người sinh sống với đầy đủ nhà ở, tạo nên một thành phố trên nước thực thụ.

![](https://cdn.beekka.com/blogimg/asset/202411/bg2024111008.webp)

Giờ đây khi dầu cạn, thành phố này đang dần hoang phế và xuống cấp trầm trọng.

![](https://cdn.beekka.com/blogimg/asset/202411/bg2024111009.webp)

## Trích dẫn

1\.

Hãng giày Allbirds vừa tuyên bố chuyển mình thành công ty AI, lập tức cổ phiếu tăng vọt gấp 5 lần chỉ trong một ngày. Nó làm tôi nhớ đến câu chuyện tương tự năm 2017 của một hãng trà đá, chỉ cần gắn mác "blockchain" là giá trị công ty tăng chóng mặt, dù sau đó phá sản trước khi kịp làm gì.

-- [Yahoo](https://gemini.google.com/app/1833a525ff94d60a)

2\.

Figma có gần 2000 nhân viên, còn đội ngũ phát triển Claude Design của Anthropic có lẽ chẳng quá 10 người. Trước tốc độ và chi phí của AI, các phần mềm truyền thống bỗng trở nên thật mỏng manh.

-- [Nhận định về Figma và Claude Design](https://finance.yahoo.com/quote/FIG/)

3\.

Tôi mơ về một tương lai không quá xa lạ, mà giống như một bản điền viên hiện đại. Ở đó, chúng ta quay lại lối sống truyền thống nhưng vẫn tận hưởng sự tiện lợi của công nghệ mới mà chẳng cần phải dán mắt vào màn hình suốt ngày.

-- [jsomers.net](https://jsomers.net/blog/the-paper-computer)

4\.

Mỗi nền văn hóa đều tạo ra những người hùng phản chiếu nỗi lo sợ sâu thẳm nhất của mình. Thung lũng Silicon sợ nhất là tăng trưởng chững lại, nên họ tôn vinh những "siêu lập trình viên" có thể code thâu đêm để biến một ý tưởng sơ sài thành kỳ lân tỷ đô.

-- [Khúc bi tráng của những người bảo trì cổ điển](https://www.joanwestenberg.com/the-rime-of-the-ancient-maintainer/)

(Hết)
