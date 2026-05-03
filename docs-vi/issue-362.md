---
date: 2025-08-22
tags: ["github", "system design", "thiết kế hệ thống", "database", "backend", "ai", "google", "javascript", "vscode", "apple"]
---

# Kỹ sư GitHub bàn về thiết kế hệ thống

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025082101.webp)

"Stellar Return", con tàu thu hồi tên lửa đầu tiên của Trung Quốc, đã chính thức hạ thủy trong tháng này. Với boong tàu rộng 40m x 60m, nó sẽ là bãi đáp di động cho tên lửa trên biển. Chủ sở hữu của con tàu là i-Space, một công ty hàng không vũ trụ tư nhân. ([via](https://www.geekpark.net/news/352799))

## Kỹ sư GitHub bàn về thiết kế hệ thống

Tuần trước, tôi tình cờ đọc được một bài viết rất hay của Sean Goedecke, kỹ sư cấp cao tại GitHub.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081814.webp)

Bài viết có tiêu đề: ["Những gì tôi biết về một thiết kế hệ thống tốt"](https://www.seangoedecke.com/good-system-design/).

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081818.webp)

Sau khi đọc xong, tôi thấy những kinh nghiệm mà Sean đúc kết thực sự rất đáng để học hỏi. Đây không phải là những lý thuyết suông mà là những bài học thực chiến từ một kỹ sư làm việc tại một trong những hệ thống lớn nhất thế giới. Dưới đây là vài điểm cốt yếu mà tôi trích dẫn lại.

Thiết kế chương trình (programming) là lắp ráp mã nguồn, còn thiết kế hệ thống (system design) là lắp ráp các dịch vụ.

Các thành phần của thiết kế chương trình là biến, hàm, lớp... trong khi các thành phần của thiết kế hệ thống là máy chủ, cơ sở dữ liệu, bộ nhớ đệm, hàng đợi, bus sự kiện và proxy.

Một hệ thống được coi là thiết kế tốt nếu nó không gặp lỗi trong một thời gian dài. Nhưng nó sẽ là một thiết kế xuất sắc nếu khi nhìn vào mã nguồn, bạn phải thốt lên: "Ồ, nó đơn giản hơn tôi nghĩ nhiều", hoặc "Phần này tôi chẳng cần bận tâm, vì dù có lỗi cũng rất dễ xử lý".

Mọi thiết kế hệ thống tốt luôn bắt đầu từ một hệ thống đơn giản và hiệu quả. Đừng bao giờ mơ mộng thiết kế một hệ thống phức tạp ngay từ con số không.

Điểm khó nhất của thiết kế hệ thống nằm ở "trạng thái" (state). Hãy cố gắng sử dụng các thành phần không lưu trạng thái (stateless) càng nhiều càng tốt và tối thiểu hóa số lượng các thành phần có lưu trạng thái. Sự phức tạp của trạng thái nằm ở chỗ bạn không thể chỉ đơn giản là khởi động lại dịch vụ khi gặp lỗi. Thông thường, bạn sẽ phải can thiệp thủ công để khôi phục trạng thái đó.

Trạng thái cần được lưu trữ trong cơ sở dữ liệu. Đây là thành phần quan trọng nhất để quản lý trạng thái. Mục tiêu thiết kế của cơ sở dữ liệu là làm sao để mỗi bảng đều dễ hiểu: chỉ cần nhìn vào cấu trúc bảng là biết nó lưu gì và tại sao lại lưu như vậy. Đừng cố tạo ra những cấu trúc bảng phức tạp, điều đó chỉ mang lại sự rắc rối cho mã nguồn và gây nghẽn hiệu năng.

Cơ sở dữ liệu thường là nút thắt cổ chai của hệ thống, vì mỗi yêu cầu trang web có thể gọi đến cơ sở dữ liệu hàng chục, thậm chí hàng trăm lần một cách tuần tự. Để tránh điều này, bạn có thể thiết kế một nút ghi (write node) và nhiều bản sao chỉ đọc (read replicas). Mọi truy vấn đọc sẽ được gửi đến các bản sao, còn lệnh ghi sẽ gửi đến nút ghi chính. Lưu ý là luôn có độ trễ đồng bộ giữa các nút. Nếu bạn vừa cập nhật một bản ghi và cần đọc lại ngay, hãy cân nhắc lưu nó vào bộ nhớ tạm để đọc ra sau khi ghi thành công.

Những tác vụ tốn thời gian nên được tách ra và xử lý như các công việc nền (background jobs) thông qua hàng đợi. Hệ thống này gồm hai phần: dịch vụ hàng đợi và bộ chạy tác vụ (worker). Bạn có thể dùng Redis cho các tác vụ cần thực hiện ngay, hoặc dùng chính cơ sở dữ liệu cho các tác vụ không quá gấp gáp.

Khi tốc độ tạo dữ liệu và tốc độ đọc dữ liệu không khớp nhau, bộ nhớ đệm (cache) là giải pháp kinh điển. Cách đơn giản nhất là lưu dữ liệu vào bộ nhớ của máy chủ, hoặc dùng các phần mềm chuyên dụng như Redis hay Memcached để nhiều máy chủ có thể chia sẻ bộ đệm. Các kỹ sư mới thường muốn cache mọi thứ, nhưng các kỹ sư kinh nghiệm lại muốn dùng cache ít nhất có thể. Bởi lẽ cache cũng là một nguồn tạo ra "trạng thái", và việc quản lý sự nhất quán cũng như thời gian hết hạn của cache là một bài toán đau đầu.

Bên cạnh cache và tác vụ nền, các hệ thống lớn thường có trung tâm sự kiện (thường dùng Kafka). Đây cũng là một dạng hàng đợi, lưu trữ thông báo rằng "một việc gì đó đã xảy ra". Ví dụ, khi người dùng đăng ký, một sự kiện "tạo tài khoản mới" sẽ được gửi vào trung tâm sự kiện. Từ đó, các dịch vụ khác như gửi email chào mừng, thiết lập không gian cá nhân... sẽ nhận thông báo và thực hiện nhiệm vụ của mình. Tuy nhiên, đừng lạm dụng sự kiện. Nhiều khi chỉ cần một dịch vụ gọi trực tiếp API của dịch vụ khác là đủ. Để dễ dàng gỡ lỗi, tốt nhất hãy tập trung toàn bộ log về một nơi để bạn có thể theo dõi phản hồi giữa các dịch vụ một cách tức thì.

Nếu dữ liệu cần được truyền đến nhiều nơi, bạn có hai lựa chọn: kéo (pull) hoặc đẩy (push). Nhìn chung, cơ chế "kéo" đơn giản hơn (như kiểu polling), còn "đẩy" thì tiết kiệm tài nguyên hơn vì máy chủ chỉ gửi dữ liệu khi có sự thay đổi. Nếu bạn cần cung cấp dữ liệu mới nhất cho 1 triệu khách hàng (như Gmail), việc chọn "đẩy" hay "kéo" phụ thuộc vào kịch bản cụ thể. Với cơ chế đẩy, bạn sẽ cần một hàng đợi sự kiện khổng lồ và một đội quân xử lý để đẩy dữ liệu đi. Với cơ chế kéo, bạn sẽ cần triển khai hàng trăm máy chủ cache tốc độ cao để xử lý lưu lượng truy cập đọc khổng lồ.

## Hai sản phẩm AI mới từ Google

Tuần này Google đã giới thiệu hai sản phẩm mới khá ấn tượng.

1. [Mô hình Imagen 4](https://aistudio.google.com/prompts/new_image)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081708.webp)

Đây là mô hình tạo ảnh từ văn bản mới nhất của Google, hiện có thể [sử dụng miễn phí](https://aistudio.google.com/prompts/new_image) trên trang web chính thức. Theo cảm nhận của tôi, tốc độ tạo ảnh rất nhanh và kết quả cực kỳ ấn tượng (như hình minh họa robot cầm ván trượt màu đỏ bên dưới).

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081707.webp)

2. [Learning About](https://learning.google.com/experiments/learn-about/signup)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081805.webp)

Learning About là một nền tảng học tập kiểu mới của Google, sử dụng AI để tạo ra các lộ trình học tập tương tác. Bạn chỉ cần nhập chủ đề muốn tìm hiểu, ví dụ như ngôn ngữ lập trình Java.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081806.webp)

Hệ thống sẽ trả về một bộ tài liệu hướng dẫn đơn giản.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081807.webp)

Ngoài phần giới thiệu tổng quát, nó còn liệt kê các chủ đề liên quan để bạn có thể đào sâu nghiên cứu thêm.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081808.webp)

## Tin tức công nghệ

1. Bộ Nội vụ Anh thông báo sẽ lắp đặt hệ thống nhận diện khuôn mặt trên các xe cảnh sát tuần tra.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081815.webp)

Khi xe di chuyển, hệ thống sẽ tự động quét khuôn mặt người đi đường và đối chiếu với cơ sở dữ liệu tội phạm. Nếu phát hiện nghi phạm, nó sẽ phát cảnh báo ngay lập tức. Trong giai đoạn thử nghiệm tại London, công nghệ này đã giúp bắt giữ 580 nghi phạm trong vòng 12 tháng.

2. Nhiều người vẫn giữ thói quen gửi bưu thiếp khi đi du lịch. Nhưng việc viết tay bưu thiếp chỉ truyền tải được văn bản và có vẻ hơi lỗi thời trong thời đại smartphone.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081302.webp)

Một công ty Mỹ vừa ra mắt dịch vụ [Keeps](https://www.sendkeeps.com/). Người dùng tải ảnh lên trang web và để lại một đoạn tin nhắn thoại.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081303.webp)

Hệ thống sẽ in ảnh thành bưu thiếp, kèm theo một mã QR ở mặt sau và gửi đến địa chỉ người nhận. Khi nhận được, người đó chỉ cần quét mã QR là có thể nghe được giọng nói của bạn.

3. Wikipedia có rất nhiều phiên bản ngôn ngữ. Bạn có đoán được bài viết nào có nhiều ngôn ngữ nhất không? Thật bất ngờ, đó là bài viết về một nghệ sĩ không mấy tên tuổi tên là David Woodard.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081304.webp)

Bài viết về ông có tới 335 phiên bản ngôn ngữ khác nhau, đứng đầu toàn bộ Wikipedia. Hầu hết các phiên bản này đều do một tài khoản tên Swmmng tạo ra từ cùng một địa chỉ IP trong suốt hơn 10 năm. Rõ ràng đây là một hành vi tự quảng bá bản thân. Hiện tại, hầu hết các phiên bản ngôn ngữ rác đã bị xóa, chỉ còn lại khoảng 20 ngôn ngữ chính thức.

## Bài viết

1. [Dịch vụ AI miễn phí của GitHub Models](https://github.blog/ai-and-ml/llms/solving-the-inference-problem-for-open-source-ai-projects-with-github-models/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025082008.webp)

GitHub hiện cung cấp khả năng gọi các mô hình AI miễn phí như GPT-4o, DeepSeek-R1, Llama 3 thông qua GitHub Models, dù có giới hạn về định mức sử dụng.

2. [Tạo mê cung bằng JavaScript](https://jrsinclair.com/articles/2025/joy-of-immutable-data-recursion-pure-functions-javascript-mazes/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025082006.webp)

Bài viết giới thiệu một thuật toán đơn giản để tạo ra mê cung kèm theo mã nguồn triển khai bằng JavaScript.

3. [Cloudflare không chỉ là CDN](https://magecdn.com/blog/2025/08/11/cloudflare-not-a-cdn/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081816.webp)

Cloudflare cung cấp CDN miễn phí không giới hạn băng thông, vậy tại sao họ vẫn có những gói CDN trả phí? Bài viết sẽ giải thích cho bạn những chỉ số quan trọng khác của một CDN ngoài băng thông.

4. [Cách Git xử lý các tệp tin lớn](https://tylercipriani.com/blog/2025/08/15/git-lfs/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081713.webp)

Những tệp tin nặng hàng chục MB không nên đưa trực tiếp vào kho lưu trữ Git. Giải pháp thông thường là dùng Git LFS, nhưng công cụ này khá khó dùng. Tác giả đã đưa ra một số đề xuất cải tiến.

5. [10 tiện ích VS Code hữu ích](https://www.xda-developers.com/vs-code-extensions-i-cant-live-without/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025052504.webp)

Danh sách 10 tiện ích mở rộng cho VS Code mà tác giả coi là "vật bất ly thân" trong công việc hàng ngày.

6. [Vấn đề về cửa sổ tắc nghẽn ban đầu của TCP](https://jeclark.net/articles/tcp-initcwnd/?tag=performance) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081706.webp)

Giao thức TCP có thiết kế "cửa sổ tắc nghẽn" để tự động điều chỉnh số lượng gói tin gửi đi dựa trên tình trạng mạng. Bài viết giải thích khái niệm này một cách dễ hiểu và đề xuất phương án tối ưu hơn.

## Công cụ

1. [doxx](https://github.com/bgreenwell/doxx)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081809.webp)

Công cụ dòng lệnh giúp xem nội dung tệp .docx ngay trong terminal.

2. [IntraScribe](https://github.com/weynechen/intrascribe)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081601.webp)

Nền tảng quản lý và cộng tác chuyển đổi giọng nói thành văn bản dành cho môi trường mạng nội bộ doanh nghiệp.

3. [P2P Remote Desktop](https://github.com/miroslavpejic85/p2p)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081602.webp)

Công cụ điều khiển máy chủ từ xa cho Windows cực kỳ gọn nhẹ, chỉ cần chạy file thực thi mà không cần cấu hình hay cài đặt phức tạp.

4. [CuteClock](https://github.com/AkenClub/CuteClock)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081703.webp)

Dự án phần cứng mã nguồn mở: chiếc đồng hồ thông minh dựa trên chip ESP8266, có thể hiển thị thời gian, thời tiết và hỗ trợ điều khiển bằng giọng nói.

5. [CleanYourMac](https://github.com/GitDzreal93/clean-your-mac)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081704.webp)

Ứng dụng dọn dẹp mã nguồn mở cho Mac, sử dụng AI để phân tích các tệp cần xóa một cách thông minh.

6. [Next QR Code Generator](https://github.com/chromium-style-qrcode/next-qrcode-generator)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081801.webp)

Tiện ích mở rộng mã nguồn mở cho Firefox giúp tạo mã QR cho trang web tương tự như tính năng trên Chrome.

7. [Translator](https://github.com/AnYi-0/Translator)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081802.webp)

Tiện ích dịch thuật ngoại tuyến cho Chrome, dựa trên Translator API và Language Detector API mới của trình duyệt, cho phép dịch mà không cần internet.

8. [Chuyển đổi Jupyter Notebook](https://ipynbtopdf.net/)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025082003.webp)

Trang web giúp chuyển đổi các tệp .ipynb sang định dạng PDF, HTML hoặc Python.

9. [Docker Pull Script](https://github.com/luckfu/docker_pull)

Một kịch bản Python giúp tải hình ảnh Docker từ các nguồn chỉ định, hỗ trợ tải song song và cập nhật tăng cường theo lớp (layer).

10. [Make Graph](https://makegraph.app/editor)

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025082102.webp)

Công cụ tạo biểu đồ trực tuyến hỗ trợ nhiều loại biểu đồ phổ biến và có thể xuất ra định dạng SVG. Ngoài ra còn có [ChartFromText](https://chartfromtext.com/) cho phép tạo biểu đồ trực tiếp từ dữ liệu văn bản nhập vào.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025082104.webp)

## AI

1. [OpenAI Progress](https://progress.openai.com/)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081709.webp)

Dự án chính thức của OpenAI nhằm trình diễn quá trình tiến hóa của AI qua từng năm: cùng một câu lệnh nhưng kết quả đầu ra qua các năm lại hoàn toàn khác biệt.

2. [MCP Playground](https://mcpso.cc/kchat/index.html)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081701.webp)

Ứng dụng web hoạt động như một máy khách MCP (Model Context Protocol), cho phép bạn chọn mô hình AI và máy chủ MCP để sử dụng trực tuyến.

3. [Coro Code](https://github.com/Blushyes/coro-code)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081803.webp)

Một đại lý lập trình AI (coding agent) hoạt động trong terminal, được coi là giải pháp thay thế mã nguồn mở cho Claude Code.

4. [Claude Code Status Bar Monitor](https://github.com/leeguooooo/claude-code-usage-bar)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025082005.webp)

Tiện ích cho Claude Code giúp hiển thị thời gian thực mức độ sử dụng và thời gian đặt lại giới hạn.

## Tài nguyên

1. [Kho bài đọc văn học phổ thông](https://zedex.github.io/mandarin-reading-resource/)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081705.webp)

Giao diện web cho kho tàng các bài đọc mẫu từ Đài Phát thanh Trung ương Trung Quốc, phân loại theo cấp học và học kỳ.

2. [Nền tảng kiểm tra phần cứng trực tuyến](https://volumeshader.org/zh)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081702.webp)

Trang web giúp kiểm tra trực tiếp các thành phần phần cứng như GPU, màn hình, mạng, camera, âm thanh, chuột và bàn phím.

3. [Mô phỏng kỳ thi vô tuyến điện nghiệp dư](https://github.com/AlliotTech/ham-exam-web)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025082002.webp)

Ứng dụng web giúp ôn luyện và thi thử dựa trên bộ đề mới nhất năm 2025.

4. [Citywalki](https://www.citywalki.com)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081804.webp)

Trang web cho phép bạn trải nghiệm đi bộ, lái xe hoặc bay drone tại hơn 200 thành phố trên thế giới thông qua các video Youtube chất lượng cao.

## Hình ảnh

1. [Cú lăn lốp xe dài nhất lịch sử](https://kottke.org/25/08/roll-on-you-crazy-tire)

Một nhóm nghệ sĩ đã leo lên một trong những đồi cát cao nhất ở Chile và thả một chiếc lốp xe xuống. Họ dùng drone quay lại toàn bộ quá trình xem nó có thể lăn được bao xa.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081710.webp)

Chiếc lốp đã lăn liên tục trong gần ba phút giữa sa mạc mênh mông. Video ghi lại cảnh tượng này thực sự rất hùng tráng và mang lại cảm giác giải tỏa căng thẳng kỳ lạ.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081711.webp)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081712.webp)

## Trích đoạn

1\. Câu chuyện về Steve Wozniak

Ngày 11 tháng 8 năm nay đánh dấu sinh nhật lần thứ 75 của Steve Wozniak, người đồng sáng lập Apple.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025082103.webp)

Trên diễn đàn Slashdot, khi có người bình luận bày tỏ sự tiếc nuối rằng nếu ông không bán sạch cổ phiếu Apple từ sớm thì giờ đây đã là một trong những tỷ phú giàu nhất thế giới, Woz đã trực tiếp phản hồi: "Tôi bán và tặng hết cổ phiếu Apple vì tiền bạc và quyền lực chưa bao giờ là mục đích sống của tôi. Tôi ưu tiên sự thanh thản và hạnh phúc cá nhân. Tôi đã tài trợ cho rất nhiều bảo tàng và nhóm nghệ thuật ở San Jose (nơi tôi sinh ra), và họ thậm chí còn lấy tên tôi đặt cho một con phố. Trong suốt 20 năm qua, tôi đi diễn thuyết và kiếm được khoảng 10 triệu đô. Số tiền đó là quá đủ cho nhu cầu của tôi rồi."

Câu chuyện này khiến tôi nhớ đến một cuốn sách lịch sử về Apple từng nhắc đến tính cách của Woz. Ngay từ thời sinh viên, ông đã rất thờ ơ với tiền bạc. Sau này khi đã giàu có, ông vẫn vậy. Ông không bao giờ ghi chép chi tiêu và cũng chẳng buồn nghe theo lời khuyên quản lý tài chính. Mỗi khi có ai đó tìm đến nhờ giúp đỡ, ông thường ký séc ngay tại chỗ. Khác với Steve Jobs, người luôn giữ chặt cổ phiếu của mình, Woz đã tặng 4 triệu đô giá trị cổ phiếu cho người thân và 2 triệu đô cho bạn bè. Cha của ông từng nhặt được một tờ séc trị giá 250.000 đô chưa được rút tiền trong xe của ông và phải thốt lên: "Người như nó không nên có nhiều tiền đến thế."

Có lần, Woz đến Apple thông báo: "Luật sư của tôi khuyên nên đầu tư đa dạng, nên tôi vừa mua một rạp chiếu phim." Nhưng rạp phim đó nằm ở khu ổ chuột phía Đông San Jose và chiếu phim về băng đảng, gây ra sự phản đối từ cộng đồng. Ông đã tham gia các cuộc họp cộng đồng, lắng nghe ý kiến người dân và hứa rạp của ông sẽ không chiếu phim bạo lực hay đồi trụy. Sau đó, người ta thấy ông dành cả buổi chiều ngồi một mình trong rạp tối để xem đi xem lại các bộ phim, tự mình đóng vai trò người kiểm duyệt nội dung.

## Trích dẫn

1\.

Tôi từng định viết một cuốn sách về ngôn ngữ lập trình Gleam. Nhưng thực tế là AI hiện nay có thể giải thích về Gleam cực kỳ rõ ràng và đáp ứng mọi yêu cầu của người đọc. Dù tôi tự tin mình viết hay hơn AI, nhưng tôi chẳng tìm được lý do gì để thuyết phục bản thân dành ra hàng trăm giờ đồng hồ viết một cuốn sách mà số tiền kiếm được chẳng đáng là bao. Có lẽ trong tương lai, động lực duy nhất để người ta viết sách là vì niềm vui thuần túy mà thôi.

-- [Cuộc khủng hoảng danh tính do AI gây ra](https://dusty.phillips.codes/2025/06/08/my-ai-driven-identity-crisis/)

2\.

Điều khiến tôi không thể phủ nhận là làm việc với các đối tác Trung Quốc dễ dàng hơn bất kỳ nơi nào khác trên thế giới. Tôi gửi email cho một người ở Trung Quốc, họ chắc chắn sẽ phản hồi trong vòng 24 giờ, thậm chí thường là chỉ trong vòng 4 giờ. Trong khi đó, gửi email cho một công ty ở Mỹ hay EU, bạn thường phải đợi vài ngày. Với các công ty Trung Quốc, tôi chưa bao giờ gặp tình trạng đó, dù chỉ một lần. Hơn nữa, các nền tảng B2B của họ luôn có đội ngũ hỗ trợ trực tuyến 24/7.

-- Một độc giả trên [Hacker News](https://news.ycombinator.com/item?id=44936016)

3\.

AI không giúp giảm bớt nỗ lực bạn cần bỏ ra để làm chủ một kỹ năng mới, nó chỉ mang lại cho bạn một ảo tưởng rằng mình đã biết thứ đó mà không cần phải thực sự học nó.

-- [AI tạo ra cảm giác kiểm soát giả tạo](https://playtechnique.io/blog/ai-doesnt-lighten-the-burden-of-mastery.html)

4\.

Những chương trình đáng tin cậy và minh bạch thường không nằm trong mục tiêu ưu tiên của những người thiết kế ra chúng.

-- [Niklaus Wirth](https://en.wikiquote.org/wiki/Niklaus_Wirth), nhà khoa học máy tính lỗi lạc, người đạt giải Turing
