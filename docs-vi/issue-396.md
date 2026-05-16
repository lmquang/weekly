---
date: 2026-05-15
tags: ["internet", "mạng lưới", "lora", "meshtastic", "ai", "trí tuệ nhân tạo", "monkeycode", "lập trình", "programming", "robot"]
---

# Giải pháp thay thế cho truyền thông Internet

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051414.webp)

"Trung tâm Tiểu cầu Tân Xương" (Xinchang Little Ball Center) tại huyện Tân Xương, tỉnh Chiết Giang, là một công trình tích hợp khách sạn, trung tâm thương mại, nhà thi đấu, sân vận động và đường đi bộ rèn luyện sức khỏe ngoài trời vào trong cùng một khối kiến trúc. ([via](https://www.archdaily.cn/cn/1036435/xin-chang-xiao-qiu-zhong-xin-line-plus-studio))

## Giải pháp thay thế cho truyền thông Internet

Một sáng sớm thức dậy, bạn nhận ra Internet đã bị cắt, bạn sẽ làm gì?

Ý tôi là sự gián đoạn triệt để, Internet hoàn toàn không hoạt động, cả thành phố không thể truy cập mạng. Tuy xác suất xảy ra sự kiện này rất thấp, nhưng không phải là không thể, ví dụ như khi gặp thiên tai hoặc chiến tranh.

Giả sử việc khôi phục truyền thông không thể diễn ra sớm, liệu có giải pháp nào thay thế không? Nói cách khác, **làm thế nào để chúng ta tự thiết lập mạng lưới**.

Dù Internet có cấu trúc phi tập trung và việc tạo ra một mạng con (subnet) không khó, nhưng để tạo ra một mạng con quy mô lớn, đủ sức chứa một nhóm bạn bè phân tán khắp nơi, vẫn là một thử thách lớn. Dù kết nối qua router không dây, dây điện thoại, Bluetooth hay tự kéo cáp quang, độ khó và chi phí đều không hề thấp.

Hôm nay, tôi muốn chia sẻ một giải pháp thiết lập mạng lưới đơn giản nhất mà tôi biết.

1. Phạm vi bao phủ lên tới hàng chục km, thậm chí xa hơn.
1. Không cần lắp đặt bất kỳ dây cáp nào, tự phát tín hiệu không dây.
1. Nguồn điện chỉ cần một viên pin dự phòng, thậm chí là một viên pin đơn lẻ.
1. Giá thành rất rẻ, một bộ thiết bị đầy đủ (đầu phát + đầu nhận) chỉ tốn tối đa vài trăm nhân dân tệ.

Nhược điểm duy nhất là băng thông khá hẹp, không thể dùng để lướt web, càng không thể xem video, chỉ có thể gửi và nhận thông tin văn bản.

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051412.webp)

Giải pháp này được gọi là LoRa, hay chính xác hơn, giao thức truyền thông của nó là LoRa, viết tắt của "Long Range" (Khoảng cách xa).

Giao thức LoRa được phát minh chuyên biệt cho truyền thông tầm xa. Chỉ với thiết bị nhỏ gọn và một ít năng lượng, nó có thể phát tín hiệu không dây ra xung quanh, giống như một đài phát thanh cá nhân. Thuật toán mã hóa của nó đặc biệt chú trọng vào khả năng chống nhiễu, ngay cả khi tín hiệu rất yếu vẫn có thể giải mã được, nhờ đó có thể nhận được từ khoảng cách xa.

Bản thân nó chỉ là một giao thức tín hiệu không dây, chúng ta cần tự hiện thực thiết bị gửi/nhận để thực hiện mã hóa và giải mã. Dự án mã nguồn mở [Meshtastic](https://meshtastic.org) đã làm điều này, quy định các giao diện phần cứng và phần mềm, đồng thời cung cấp các giải pháp thiết bị cụ thể.

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051413.webp)

Mọi thứ trở nên rất đơn giản. **Bạn chỉ cần tìm các thiết bị tương thích với Meshtastic, mỗi người sở hữu một cái, là có thể tạo thành một mạng lưới truyền thông đơn giản**. Hệ thống sẽ tự động chuyển tiếp tin nhắn theo dạng mạng lưới (mesh) giữa tất cả các nút.

Trên các trang thương mại điện tử, thiết bị đầu cuối Meshtastic có giá dao động từ vài chục đến vài trăm nhân dân tệ. Vì là hệ thống mã nguồn mở, bất kỳ nhà sản xuất nào cũng có thể tạo ra các thiết bị tương thích. Trang web chính thức có một [danh sách thiết bị](https://meshtastic.org/docs/hardware/devices/) để tham khảo, dưới đây là hình dáng của một vài loại thiết bị.

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051005.webp)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051007.webp)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051006.webp)

Trang chủ cũng cung cấp [phần mềm client](https://meshtastic.org/docs/software/) cho nhiều nền tảng khác nhau, dưới đây là giao diện trên điện thoại di động.

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051004.webp)

Như đã đề cập, thiết bị này tiêu thụ điện năng rất thấp, chỉ cần một viên pin dự phòng là có thể sử dụng trong thời gian dài (từ vài ngày đến vài tuần). Nếu đi kèm với tấm pin năng lượng mặt trời mini, nó có thể duy trì kết nối vĩnh viễn.

Khoảng cách truyền tải giữa hai nút trong phạm vi 5km là hoàn toàn khả thi. Nếu các tòa nhà không quá dày đặc, con số này có thể lên tới 10km đến 15km. Ở những khu vực trống trải (như mặt nước), khoảng cách có thể đạt tới hàng chục km hoặc xa hơn. Khi mạng lưới có nhiều nút, tin nhắn sẽ được truyền tiếp sức, giúp khoảng cách truyền đi xa hơn nữa.

Tổng hợp lại, đây có lẽ là giải pháp thiết lập mạng lưới truyền thông cá nhân đơn giản, thực dụng và rẻ tiền nhất hiện nay. Nó không thể thay thế việc duyệt web, nhưng hoàn toàn có thể thay thế chức năng nhắn tin của Internet.

## MonkeyCode: Nền tảng phát triển AI mã nguồn mở

Các công ty mô hình lớn đều có giao diện web để bạn sử dụng mô hình trực tuyến.

Hôm nay tôi muốn giới thiệu một dự án mã nguồn mở mang tên [MonkeyCode](https://github.com/chaitin/MonkeyCode/), giúp bạn tự thiết lập giao diện web AI như vậy (hình dưới), dự án này hiện đã đạt gần 3000 sao trên GitHub.

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051203.webp)

Nó tích hợp đầy đủ các chức năng lập trình AI, bạn không cần sử dụng thêm công cụ khác, không cần thiết lập môi trường hay chuyển đổi qua lại, chỉ cần mở trình duyệt và đưa ra yêu cầu bằng một câu lệnh.

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051101.webp)

Thông qua giao diện web, bạn có thể **tạo nhiều máy ảo** ngay trên máy chủ lưu trữ, mỗi dự án AI khác nhau sẽ chạy trên một máy ảo riêng biệt. Nó cung cấp sẵn nhiều loại image hệ điều hành cho các máy ảo này.

MonkeyCode còn hỗ trợ cấu hình thông báo qua DingTalk, Lark (Feishu), WeChat Work, Webhook, cũng như liên kết với các kho lưu trữ GitHub, GitLab, Gitee, Gitea.

Ngoài việc tự triển khai, dự án còn cung cấp [môi trường phát triển trên đám mây](https://monkeycode-ai.com/console) miễn phí, hỗ trợ điều khiển trên cả điện thoại và máy tính.

Hạn mức miễn phí cho môi trường đám mây là 20 triệu Token mỗi ngày, ngoài ra còn cung cấp nhiều mô hình như GPT 5.5 để người dùng sử dụng (yêu cầu tích điểm).

## Reverse Captcha: Captcha ngược

Captcha trên các trang web thường được dùng để xác nhận khách truy cập là người thật, không phải robot.

Hiện nay, thư viện vận hành trình duyệt mã nguồn mở Browser-use đã đưa ra khái niệm [Reverse Captcha](https://browser-use.com/posts/prove-you-are-a-robot). Loại Captcha này ngăn chặn người thật và chỉ cho phép AI robot đi qua, thường được sử dụng cho các API chỉ dành riêng cho AI.

Dưới đây là một bài toán toán học đóng vai trò như một Captcha ngược.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026042007.webp)

Với những câu hỏi như vậy, người thật nhìn vào sẽ không hiểu gì, nên đương nhiên không thể trả lời. Tuy nhiên, các mô hình lớn có thể loại bỏ các chữ cái in hoa, các ký tự ngẫu nhiên và khoảng trắng để đọc hiểu đề bài gốc:

> Hai đoàn tàu đang di chuyển ngược chiều nhau trên một đường ray thẳng có chiều dài d với vận tốc v1 và v2. Một con chim bắt đầu bay từ một đoàn tàu với vận tốc vb đến đoàn tàu kia, sau đó quay đầu bay ngược lại, cứ tiếp tục như vậy cho đến khi hai đoàn tàu gặp nhau. Hỏi con chim đã bay được tổng cộng bao xa?

Sau khi đọc hiểu đề bài, mô hình lớn sẽ áp dụng công thức toán học để tính ra đáp án, từ đó vượt qua Captcha.

## Tin tức công nghệ

1. [Định nghĩa lại con trỏ chuột](https://deepmind.google/blog/ai-pointer/)

Kể từ khi được phát minh, con trỏ chuột luôn đại diện cho vị trí thao tác hiện tại của người dùng.

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051303.webp)

Google đã đề xuất một phương án mới, thay đổi ý nghĩa của con trỏ chuột.

Trong tương lai, con trỏ chuột sẽ chỉ được dùng để hiển thị trực quan quy trình thao tác của AI, giúp người dùng thấy được AI đang làm gì tại thời điểm đó.

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051304.webp)

Điều này cũng đồng nghĩa với việc người dùng sẽ không còn di chuyển chuột khi làm việc với mô hình AI, mà thay vào đó sẽ dựa vào bàn phím hoặc giọng nói để đưa ra các lệnh thao tác.

2. [Tái chế dây đồng cũ](https://www.bloomberg.com/news/articles/2024-05-29/telcos-hunt-down-billions-worth-of-buried-copper-as-prices-soar)

Kỷ nguyên năng lượng mới rất cần đồng. Xe điện, điện mặt trời, điện gió... tất cả đều cần đến dây dẫn làm từ đồng.

Trong vài năm qua, giá đồng đã tăng vọt, kéo theo việc tái chế dây đồng cũ trở thành một ngành kinh doanh béo bở.

![](https://cdn.beekka.com/blogimg/asset/202405/bg2024053107.webp)

Các đường dây điện thoại và dây mạng trước đây sử dụng lượng lớn đồng, nay phần lớn đã bị bỏ không và được thay thế bằng cáp quang hoặc điện thoại di động. Ngoài ra, dưới lòng đất còn rất nhiều cáp điện cũ không còn sử dụng, hay trong các máy điều hòa cũ cũng chứa rất nhiều đồng.

![](https://cdn.beekka.com/blogimg/asset/202405/bg2024053106.webp)

Nếu số đồng này có thể được thu hồi, đó sẽ là một khối tài sản khổng lồ. Hơn nữa, việc tái chế đồng rất đơn giản, chỉ cần loại bỏ lớp vỏ bảo vệ bên ngoài là có được dây đồng với độ tinh khiết cao.

Có thể dự đoán rằng, tái chế đồng sẽ trở thành một ngành nghề chuyên biệt trong các đô thị.

3. [Robot giao hàng chiếm dụng vỉa hè](https://blockclubchicago.org/2025/12/08/delivery-robots-take-over-chicago-sidewalks-sparking-debate-and-a-petition-to-hit-pause/)

Tại thành phố Chicago, Mỹ, việc sử dụng robot giao hàng với số lượng lớn trong khu vực nội đô đã gây ra sự phản đối từ cư dân.

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120917.webp)

Lý do là robot giao hàng đi trên vỉa hè chứ không phải dưới lòng đường, gây cản trở người đi bộ.

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120918.webp)

Một người dân cho biết: "Vỉa hè là dành cho con người, không phải cho robot giao hàng. Một khu dân cư yên tĩnh mà xuất hiện hàng chục, thậm chí hàng trăm chiếc xe như vậy, rồi nó sẽ trở thành cái gì?"

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120919.webp)

Đây thực sự là một vấn đề đáng suy ngẫm, liệu con người có thực sự muốn đi bộ cùng robot không? Bạn có thể chấp nhận người đi bộ bên cạnh mình là một cỗ máy?

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120920.webp)

## Bài viết

1. [Tại sao ID theo dõi phải dài 128 bit?](https://newsletter.signoz.io/p/why-should-a-trace-id-be-128-bits) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026050901.webp)

Nếu bạn cần tạo ID ngẫu nhiên cho người dùng, tốt nhất là nên sử dụng độ dài 128 bit, nếu không, theo lý thuyết xác suất, (đối với các dịch vụ có lượt truy cập lớn) rất có thể sẽ xảy ra xung đột ID.

2. [AI nên xuất kết quả dưới dạng HTML](https://simonwillison.net/2026/May/8/unreasonable-effectiveness-of-html/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026050902.webp)

Hiện tại AI thường xuất kết quả dưới định dạng Markdown. Bài viết này cho rằng nên sử dụng định dạng HTML, nhờ đó AI có thể chèn các biểu đồ SVG, các thành phần tương tác, điều hướng trong trang... để truyền tải nhiều thông tin hơn.

3. [Tôi rất lo lắng cho Bun](https://wwj.dev/posts/i-am-worried-about-bun/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026050905.webp)

Bun là một JS runtime vừa được Anthropic mua lại vào tháng 12 năm 2025. Tác giả lo ngại rằng trong tương lai nó sẽ tràn ngập code do AI tạo ra, dẫn đến chất lượng giảm sút.

4. [Làm thế nào để bảo vệ khóa SSH private?](https://ahelwer.ca/post/2026-05-08-builtin-u2f/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051001.webp)

Mã độc ngày càng nhiều và rất khó phòng bị. Bài viết này (ở phần sau) hướng dẫn bạn cách sử dụng cơ chế bảo mật có sẵn của máy tính để bảo vệ khóa SSH private, yêu cầu vân tay hoặc nhận diện khuôn mặt để đọc khóa, giúp nó không dễ bị đánh cắp.

5. [Tôi đã mở cổng 22 trong suốt 54 ngày](https://arman-bd.hashnode.dev/i-left-port-22-open-on-the-internet-for-54-days-here-s-who-showed-up) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051003.webp)

Cổng 22 là cổng đăng nhập SSH và thường xuyên bị tấn công. Tác giả đã sử dụng một "honeypot" (bẫy mật) để mở cổng này, xem điều gì sẽ xảy ra và các hacker đột nhập vào hệ thống đã thực thi những lệnh gì.

6. [Sự khác biệt giữa Ibuprofen và Tylenol](https://asteriskmag.com/issues/14/the-mystery-in-the-medicine-cabinet) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051202.webp)

Ibuprofen và Tylenol đều là những thuốc hạ sốt, giảm đau phổ biến. Bài viết giới thiệu sự khác biệt giữa hai loại này. Tác giả cho rằng, chỉ cần không quá liều, Tylenol trong hầu hết các trường hợp đều tốt hơn Ibuprofen.

## Công cụ

1. [RethinkDNS](https://github.com/serverless-dns/serverless-dns)

Một máy chủ DNS mã nguồn mở có thể được triển khai trong môi trường Serverless (ví dụ như Cloudflare Worker).

2. [Pinta](https://www.pinta-project.com/)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025122501.webp)

Phần mềm xử lý hình ảnh mã nguồn mở, một lựa chọn thay thế cho Photoshop, hỗ trợ nhiều nền tảng desktop khác nhau.

3. [GitForms](https://github.com/Luigigreco/gitforms)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025121901.webp)

Ứng dụng mã nguồn mở này cho phép lưu trữ dữ liệu biểu mẫu vào GitHub issue. Điều này có nghĩa là bạn không cần backend mà vẫn có thể thu thập dữ liệu do người dùng gửi qua biểu mẫu.

4. [gecit](https://github.com/boratanrikulu/gecit)

Một công cụ dòng lệnh cài đặt trên máy tính cục bộ để giả mạo đích đến của yêu cầu mạng, tức là thay đổi trường SNI (tên miền) của gói tin.

5. [MapPoster Online](https://github.com/ianho7/maptoposter-online)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026050801.webp)

Ứng dụng web mã nguồn mở biến bản đồ thành phố thành áp phích quảng cáo.

6. [boss-agent-cli](https://github.com/can4hou6joeng4/boss-agent-cli)

Công cụ dòng lệnh cho BOSS Zhipin và Zhaopin, cho phép tìm kiếm/xem tin tuyển dụng, hỗ trợ cả vai trò ứng viên và nhà tuyển dụng, đồng thời tích hợp AI Agent.

7. [TITAN PLANET](https://github.com/ezet-galaxy/-ezetgalaxy-titan)

Một dự án khá sáng tạo, bản thân nó là một backend framework bằng JavaScript nhưng có thể biên dịch thành một gói nhị phân Rust duy nhất, từ đó cải thiện đáng kể tốc độ thực thi.

8. [qjp](https://github.com/plainas/qjp)

Một trình truy vấn JSON tương tác trên dòng lệnh, khi mở tệp JSON, nó sẽ hiển thị tất cả các mục cấp một, cho phép bạn chọn một mục và mở rộng theo dạng cây.

9. [tinypdf](https://github.com/Lulzx/tinypdf)

Một thư viện JS cực nhỏ dùng để tạo tệp PDF, chỉ nặng 3KB.

10. [edge-tts](https://github.com/rany2/edge-tts)

Một gói Python sử dụng dịch vụ giọng nói trực tuyến của Microsoft để chuyển văn bản thành giọng nói.

## Liên quan đến AI

1. [FeedFuse](https://github.com/BryanHoo/FeedFuse)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051204.webp)

Trình đọc RSS nền web được tích hợp các tính năng AI, tự động lấy toàn bộ nội dung bài viết, cung cấp bản tóm tắt và dịch thuật bằng AI.

2. [IBus LLM Pinyin Input](https://github.com/volsifly/ibus_llm_pinyin_input)

Bộ gõ Pinyin AI dựa trên IBus, sử dụng mô hình lớn để gợi ý từ dựa trên đầu vào của người dùng.

3. [kooky](https://github.com/iAmCorey/kooky)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026051301.webp)

Terminal macOS tối giản được tối ưu hóa cho AI coding, có thể khởi động nhanh các agent như Claude Code/Codex, hỗ trợ chạy chia màn hình và hiển thị trạng thái.

## Tài nguyên

1. [taken.](https://sinceyouarrived.world/taken)

Trang web này giúp bạn kiểm tra xem yêu cầu web của mình chứa bao nhiêu thông tin cá nhân.

2. [DataCenter.fm](https://datacenter.fm)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026050904.webp)

Một trình tạo âm thanh nền, mô phỏng tiếng ồn khi máy chủ trong phòng máy vận hành.

3. [MathNet](https://mathnet.mit.edu/)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026050906.webp)

Trang web do MIT duy trì, thu thập hơn 30.000 bài toán toán học.

4. [Các định luật về UX](https://lawsofux.com/)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026050907.webp)

Trang web tổng hợp nhiều định luật về trải nghiệm người dùng (UX), ví dụ như [Định luật Miller](https://lawsofux.com/millers-law/): Một người bình thường chỉ có thể ghi nhớ khoảng 7 mục (dao động trong khoảng 5-9 mục) cùng một lúc.

## Hình ảnh

1. [Ô nhiễm vệ tinh](https://apod.nasa.gov/apod/ap260427.html)

Số lượng vệ tinh trên quỹ đạo Trái Đất ngày càng nhiều, gây ảnh hưởng nghiêm trọng đến việc quan sát thiên văn vì vệ tinh phản chiếu ánh sáng, làm mờ đi các thiên thể khác.

Dưới đây là bức ảnh một sao chổi được chụp bằng phương pháp phơi sáng lâu, nhưng kết quả thu được lại toàn là vệ tinh.

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026050908.webp)

Vì vệ tinh đang di chuyển nên khi phơi sáng lâu sẽ tạo thành các đường kẻ dạng lưới. Bạn còn có thể tìm thấy sao chổi trong bức ảnh trên không?

Với sự phát triển của truyền thông vệ tinh, số lượng vệ tinh sẽ tăng theo cấp số nhân. Các nhà thiên văn học đã đề xuất việc xây dựng kính thiên văn ở mặt sau của Mặt Trăng.

## Trích đoạn

1. [Máy pha cà phê ngoài không gian](https://mceglowski.substack.com/p/bitter-lessons-from-the-isspresso)

Sau khi các phi hành gia Mỹ lên Trạm Vũ trụ Quốc tế (ISS), việc uống cà phê nóng trở nên rất khó khăn. Vì vậy, NASA đã đặt hàng một công ty của Ý chế tạo một chiếc máy pha cà phê có thể sử dụng được trong không gian.

Công ty Ý này nhanh chóng nhận ra rằng nhiệm vụ này vô cùng khó khăn.

Mỗi bộ phận của máy pha cà phê đều phải được thiết kế lại để đảm bảo không gây nguy hiểm cho phi hành gia và trạm vũ trụ: nó không được làm hỏng hệ thống điện, không được làm nhiễu liên lạc vô tuyến, không được rò rỉ nước sôi, không được gây cháy, không được phát ra ánh sáng quá chói, không được gây giật điện, không được quá nhiệt, không được gây tiếng ồn lớn, không được giải phóng khí độc và không được tỏa mùi lạ.

Đặc biệt khó khăn là những điểm sau:

(1) Máy pha cà phê phải chịu được các tác động vật lý, chủ yếu là gia tốc trong quá trình phóng tên lửa.

(2) Trạm vũ trụ không có sự đối lưu không khí, nên máy phải có hệ thống tản nhiệt riêng biệt để tránh quá nhiệt gây cháy.

(3) Trong môi trường không trọng lực, máy không được để chất lỏng tràn ra ngoài, không được để hơi nước sôi lan tỏa khắp khoang tàu.

(4) Máy pha cà phê không được có các cạnh sắc nhọn để tránh làm phi hành gia bị thương.

Sau nhiều lần lập luận, thử nghiệm và kiểm tra, chiếc máy pha cà phê không gian cuối cùng đã ra đời và được đưa lên ISS vào năm 2015.

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026050911.webp)

Dưới Trái Đất, một chiếc máy pha cà phê cơ bản có giá khoảng 150 USD và nặng 3,5 kg. Trong khi đó, chiếc máy pha cà phê không gian nặng tới 20 kg và chi phí có thể lên tới hàng triệu USD.

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026050912.webp)

Cà phê nó tạo ra được đựng trong các túi mềm và người uống sẽ bóp túi để thưởng thức.

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026050913.webp)

2. [Đừng tin rằng "những người không dùng AI sẽ lạc hậu"](https://migrainebrain.bearblog.dev/people-who-dont-use-ai-will-be-left-behind/)

Có người nói: "Những người không sử dụng AI sẽ bị thời đại bỏ lại phía sau." Tôi rất ghét kiểu nói này, vì tôi tin chắc rằng thực tế hoàn toàn ngược lại.

Những người quá phụ thuộc vào AI cuối cùng sẽ bị thời đại đào thải. Họ sẽ quên cách suy nghĩ, cách viết lách, cách thực hiện những tìm kiếm đơn giản nhưng đáng tin cậy, và cách phân biệt giữa sự thật và hư cấu...

Họ sẽ quên mất cách học hỏi, và tôi nghĩ đó mới là điều khiến tôi buồn nhất. Bản thân việc học hỏi là một điều tuyệt vời biết bao.

Nếu bạn tin rằng AI có thể làm tốt hơn mình, điều bạn cần làm không phải là phó mặc mọi thứ cho AI, mà là nỗ lực để trở nên mạnh mẽ hơn trong những lĩnh vực mà AI không thể chạm tới.

## Trích dẫn

1\.

Mỗi năm có 1,5 tỷ chiếc điện thoại thông minh được bán ra trên toàn thế giới, phần lớn trong số đó được sử dụng chưa đầy hai năm rồi bị vứt bỏ hoặc để không.

Đây là một sự lãng phí tài nguyên tính toán khổng lồ. Cấu hình của điện thoại thông minh hiện đại ngày càng cao, hoàn toàn có thể được tận dụng để nâng cao năng lực tính toán toàn cầu.

-- [《Tái sử dụng điện thoại thông minh cũ》](https://arxiv.org/abs/2110.06870)

2\.

Ngôn ngữ lập trình trong tương lai sẽ không phải là ngôn ngữ mà bạn dễ làm chủ nhất, mà là ngôn ngữ mà AI dễ làm chủ nhất.

-- [@RealRichomie](https://x.com/RealRichomie/status/2047509168442196230)

3\.

Sáng tạo có suy giảm theo tuổi tác không?

Một nghiên cứu tại Mỹ chỉ ra rằng, sáng tạo được chia làm hai loại: khả năng đổi mới mang tính liên tưởng thường tăng dần theo tuổi tác, trong khi khả năng đổi mới mang tính đột phá lại có xu hướng giảm xuống.

-- [《Tiến bộ khoa học luôn phải đánh đổi bằng những đám tang》](https://nautil.us/is-this-why-science-advances-one-funeral-at-a-time-1280650)

4\.

Các mô hình lớn là một sự nén có mất mát dữ liệu huấn luyện, và dữ liệu huấn luyện lại là một sự lấy mẫu có mất mát từ thế giới thực.

Khi AI tạo ra kết quả đầu vào, nó cần lấp đầy những thông tin bị mất trong quá trình nén, rồi "bơm căng" chúng thành các bài viết, hình ảnh, phần mềm hay video.

-- [《Công cụ thổi phồng》](https://mattstromawn.com/writing/expansion-artifacts/)
