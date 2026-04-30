# Không có dữ liệu, mô hình lớn chỉ là "kẻ ngốc"

Đây là nơi ghi lại những nội dung công nghệ đáng chia sẻ hàng tuần, xuất bản vào mỗi thứ Sáu.

Tạp chí này là [nguồn mở](https://github.com/ruanyf/weekly), rất hoan nghênh các bạn [đóng góp nội dung](https://github.com/ruanyf/weekly/issues). Ngoài ra còn có dịch vụ ["Ai đang tuyển dụng"](https://github.com/ruanyf/weekly/issues/9088), nơi đăng tải thông tin tuyển dụng lập trình viên. Để hợp tác, vui lòng [liên hệ qua email](mailto:yifeng.ruan@gmail.com) (yifeng.ruan@gmail.com).

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032201.webp)

Hệ thống hành lang rực rỡ sắc màu tại một khu dân cư ở Nhật Chiếu, Sơn Đông. Ngay lối vào giữa rừng cây còn có một quán cà phê xinh xắn. ([via](https://mooool.com/coffee-tree-canopy-by-selgascano.html))

## Không có dữ liệu, mô hình lớn chỉ là "kẻ ngốc"

Nếu bây giờ làm một cuộc khảo sát với câu hỏi: "Bạn có nghĩ các mô hình ngôn ngữ lớn (LLM) thực sự thông minh không?" Tôi tin rằng đa số sẽ trả lời là có. Ngay cả khi AI vẫn đang ở giai đoạn sơ khai, khả năng thay thế con người trong nhiều công việc trí tuệ của nó vẫn là điều vô cùng kỳ diệu.

Tuy nhiên, chúng ta đừng quên bản chất thực sự: **Mô hình lớn không phải là phép thuật, càng không phải là những "thực thể trí tuệ silicon" có ý thức. Chúng là các mô hình ngôn ngữ dựa trên quy luật thống kê**, mọi hành vi đều xuất phát từ các phép tính toán học.

Bằng chứng rõ nhất là nếu bạn đưa cho nó một bài toán chưa từng xuất hiện trong dữ liệu huấn luyện – tức là không có quy luật thống kê sẵn có – nó sẽ hoàn toàn bó tay. Đó chính là nội dung của một [thí nghiệm](https://esolang-bench.vercel.app/) thú vị mà tôi muốn chia sẻ hôm nay.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032008.webp)

Hai nhà nghiên cứu nước ngoài đã chọn ra năm mô hình lớn phổ biến nhất: GPT-5.2, O4-mini, Gemini 3 Pro, Qwen3-235B và Kimi K2. Họ yêu cầu các mô hình này sử dụng năm ngôn ngữ lập trình cực kỳ hiếm gặp – Brainfuck, Befunge-98, Whitespace, Unlambda và Shakespeare – để giải quyết các bài toán khác nhau.

Đặc điểm chung của các ngôn ngữ này là tài liệu trên mạng cực kỳ khan hiếm, vì vậy chúng gần như không xuất hiện trong tập dữ liệu huấn luyện của AI. Kết quả thế nào bạn đoán được chứ?

Nói một cách ngắn gọn: AI thể hiện vô cùng tệ hại. Tỷ lệ trả lời đúng trung bình của năm mô hình này chỉ đạt vỏn vẹn 3,8%, tức là **cứ 100 câu thì chỉ đúng chưa đầy 4 câu**. Trong khi đó, với Python, tỷ lệ này thường đạt trên 90%.

Đáng buồn hơn, vài câu trả lời đúng ít ỏi đó đều nằm ở mức độ cực kỳ sơ đẳng. Với các bài toán ở mức trung bình và nâng cao, tỷ lệ chính xác của cả năm "siêu AI" đều bằng không.

Thí nghiệm này chứng minh một điều: **Trí thông minh của mô hình lớn trước hết được quyết định bởi dữ liệu huấn luyện**. Càng nhiều dữ liệu, nó càng giỏi (như Python); càng ít dữ liệu, nó càng tỏ ra ngây ngô và chẳng làm được việc gì nên hồn.

Vậy một câu hỏi thú vị đặt ra là: Nếu một ngôn ngữ hiếm không có dữ liệu trên mạng, nhưng chúng ta cung cấp cho AI một cuốn "Sổ tay hướng dẫn" chi tiết, liệu nó có thể học cách lập trình bằng ngôn ngữ đó ngay lập tức không?

## MAI-Image-2

Tuần này, Microsoft đã ra mắt mô hình tạo ảnh của riêng mình mang tên [MAI-Image-2](https://microsoft.ai/news/introducing-MAI-Image-2/).

Nhiều [đánh giá](https://decrypt.co/361791/microsoft-mai-image-2-text-image-model-review) cho rằng chất lượng hình ảnh của nó rất cao, hiện chỉ đứng sau nano-banana-2 của Google. Microsoft cũng đã mở trang web [MAI Playground](https://playground.microsoft.ai/chat) để người dùng trải nghiệm miễn phí.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032009.webp)

Tôi đã dùng thử và thấy độ chi tiết của ảnh thực sự ấn tượng, trông rất thật. Ví dụ như bức hình "một chú chó đạp xe dưới biển" dưới đây.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032010.webp)

Tuy nhiên, nó có khá nhiều hạn chế: (1) Từ chối tạo các hình ảnh nhạy cảm hoặc gây tranh cãi; (2) Hạn mức miễn phí 15 ảnh mỗi ngày, mỗi lần cách nhau 30 giây; (3) Chỉ hỗ trợ tỷ lệ khung hình 1:1; (4) Không có công cụ chỉnh sửa, chỉ đơn thuần là tạo ảnh từ văn bản.

Nếu bạn cần tạo ảnh chất lượng cao từ mô tả, đây là một lựa chọn đáng để thử.

## Tin công nghệ

1. [Trang bìa có thể chơi được](https://www.yankodesign.com/2026/03/16/red-bull-just-put-a-playable-tetris-game-on-a-magazine-cover/)

Red Bull vừa phát hành một tạp chí trò chơi bằng giấy mang tên "GamePop".

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032002.webp)

Điểm đặc biệt nhất chính là trang bìa tích hợp trò chơi "Xếp gạch" (Tetris) hoàn toàn có thể chơi được. Đây là cuốn sách đầu tiên trên thế giới làm được điều này.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032003.webp)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032004.webp)

Bí mật nằm ở một bảng mạch linh hoạt siêu mỏng được nhúng ngay trong bìa giấy.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032005.webp)

Nó được trang bị 180 đèn LED RGB, 7 nút bấm cảm ứng điện dung và một con chip ARM 32-bit.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032006.webp)

Thậm chí nó còn có pin sạc và cổng Type-C để tiếp năng lượng.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032007.webp)

Đáng tiếc là đây là phiên bản giới hạn, chỉ có 150 bộ được đánh số thứ tự trên toàn cầu và không bán công khai.

2. [Thu phí để được gặp nhân viên hỗ trợ thật](https://arstechnica.com/gadgets/2025/02/misguided-hp-customer-support-approach-included-forced-15-minute-call-wait-times/)

Các doanh nghiệp thường không thích hỗ trợ qua điện thoại bằng người thật vì tốn kém, thay vào đó họ muốn chuyển sang trả lời tự động. HP đã nghĩ ra một cách: ép người dùng phải chờ đợi.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032203.webp)

Khi gọi đến tổng đài HP, bạn sẽ được khuyên lên trang web tự tìm câu trả lời. Nếu kiên quyết muốn gặp nhân viên, bạn phải chờ đúng 15 phút. Nếu cúp máy giữa chừng, bạn sẽ phải bắt đầu lại từ đầu. Hệ thống sẽ liên tục nhắc nhở bạn sau mỗi vài phút rằng bạn có thể gửi email hoặc truy cập web thay vì chờ đợi.

Cách làm này tuy gây khó chịu nhưng có lẽ sẽ sớm trở thành tiêu chuẩn: miễn phí thì dùng AI, muốn gặp người thật thì phải trả thêm tiền hoặc tốn thêm thời gian.

3. [Cách ném đĩa hiệu quả](https://arstechnica.com/science/2024/10/how-physics-can-improve-your-disc-golf-game/)

Làm sao để ném đĩa vừa nhanh vừa xa? Một nhà vật lý người Mỹ đã thực hiện thí nghiệm với hàng chục sinh viên để tìm ra tư thế và góc ném tối ưu.

![](https://cdn.beekka.com/blogimg/asset/202411/bg2024110510.webp)

Ông phát hiện ra rằng việc đặt ngón tay cái cách mép ngoài của đĩa khoảng 3cm sẽ cho tốc độ xoay và vận tốc ban đầu tốt nhất.

![](https://cdn.beekka.com/blogimg/asset/202411/bg2024110511.webp)

Tốc độ xoay càng cao thì vận tốc ban đầu càng lớn. Vì vậy, lần tới chơi ném đĩa, hãy chú ý vị trí ngón tay cái của bạn nhé.

## Bài viết

1. [Sự sụp đổ chậm chạp của MkDocs](https://fpgmaas.com/blog/collapse-of-mkdocs/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032304.webp)

MkDocs vốn là công cụ tạo trang tài liệu nổi tiếng, nhưng những mâu thuẫn gay gắt giữa các thành viên cốt cán đang khiến dự án này đứng trước nguy cơ tan rã.

2. [Dùng AI dự đoán thời gian cà phê nguội](https://dynomight.net/coffee/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032306.webp)

Tác giả đã yêu cầu các mô hình AI đưa ra công thức tính thời gian cà phê hạ nhiệt, sau đó tiến hành đo đạc thực tế để xem AI nào dự đoán chính xác nhất.

3. [Ứng dụng tiếp theo có thể sẽ là "không đầu" (headless)](https://tuananh.net/2026/03/18/why-your-next-mobile-app-is-probably-headless/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032202.webp)

Nếu tương lai chúng ta điều khiển điện thoại hoàn toàn qua trợ lý AI, các ứng dụng có lẽ chẳng cần giao diện hiển thị nữa, chúng chỉ cần cung cấp các cổng dữ liệu cho AI là đủ.

4. [Nén dữ liệu trên trình duyệt bằng Canvas](https://jstrieb.github.io/posts/canvas-compress/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022105.webp)

Kỹ thuật độc đáo giúp nén dữ liệu thành một hình ảnh ngay tại phía máy khách bằng cách tận dụng thẻ canvas của HTML5.

5. [Ruby là ngôn ngữ tốt nhất để xây dựng ứng dụng AI](https://paolino.me/ruby-is-the-best-language-for-ai-apps/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022406.webp)

Tác giả so sánh Python, JavaScript và Ruby khi viết một AI Agent và đưa ra kết luận rằng Ruby mang lại trải nghiệm phát triển thuận tiện nhất.

6. [Công nghệ bê tông của người La Mã cổ đại](https://unchartedterritories.tomaspueyo.com/p/how-roman-technology-drove-its-architecture) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032011.webp)

Việc phát minh ra bê tông đã giúp người La Mã tạo nên những công trình có không gian nội thất khổng lồ và cực kỳ bền vững, tồn tại đến tận ngày nay.

## Công cụ

1. [proxychains-rs](https://github.com/tianrking/proxychains-rs)

Phiên bản Rust của proxychains4, cho phép điều hướng lưu lượng của một tiến trình qua chuỗi proxy tùy chọn.

2. [Flare Stack Blog](https://github.com/du2333/flare-stack-blog)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032001.webp)

Hệ thống blog chạy trên Cloudflare Workers, tích hợp đầy đủ các dịch vụ D1, R2 và KV.

3. [Tunelo](https://github.com/jiweiyuan/tunelo)

Công cụ tạo đường hầm ánh xạ dịch vụ nội bộ ra internet chỉ với một dòng lệnh, sử dụng giao thức QUIC để đảm bảo tốc độ.

4. [ReadAny](https://github.com/codedogQBY/ReadAny)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032208.webp)

Trình đọc sách đa nền tảng tích hợp AI, hỗ trợ đọc văn bản bằng giọng nói và đồng bộ dữ liệu.

5. [RaTeX](https://github.com/erweixin/RaTeX)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032401.webp)

Công cụ hiển thị công thức toán học LaTeX viết bằng Rust, tương thích hoàn toàn với KaTeX.

6. [Work Review](https://github.com/wm94i/Work_Review)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032509.webp)

Ứng dụng giúp bạn tự động ghi lại lịch sử sử dụng máy tính trong ngày để dễ dàng tổng kết công việc.

7. [Valdi](https://github.com/Snapchat/Valdi)

Khung làm việc UI từ SnapChat, cho phép viết code theo kiểu React nhưng biên dịch ra ứng dụng gốc (native) cho iOS, Android và Mac.

8. [Npflared](https://npflared.thomas-cogez.fr/index.html)

![](https://cdn.beekka.com/blogimg/asset/202412/bg2024122502.webp)

Công cụ giúp thiết lập kho lưu trữ NPM nội bộ cho doanh nghiệp.

9. [Chokidar](https://github.com/paulmillr/chokidar)

Thư viện Node.js mạnh mẽ để theo dõi các sự kiện trên hệ thống tệp tin.

## AI

1. **Giao diện WeChat cho OpenClaw**

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032301.webp)

WeChat vừa chính thức mở cổng kết nối cho các bot AI, cho phép chúng gửi tin nhắn trực tiếp vào ứng dụng. Cộng đồng đã nhanh chóng phát triển nhiều bộ SDK để tận dụng tính năng này:

- [wechat-rs-sdk](https://github.com/tianrking/weixin-agent-rs)
- [WeChatBot](https://github.com/corespeed-io/wechatbot)
- [WeClaw](https://github.com/fastclaw-ai/weclaw)
- [WeChat-Channel](https://github.com/nanbingxyz/wechat-channel)

2. [AI CLI Complete Notify](https://github.com/ZekerTop/ai-cli-complete-notify)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032303.webp)

Công cụ thông báo khi các tác vụ dòng lệnh AI hoàn thành, hỗ trợ gửi tin nhắn qua Telegram, email hoặc các nền tảng chat doanh nghiệp.

3. [Claude Config Manager](https://github.com/Daydayoneup/ccm)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032501.webp)

Trình quản lý tài nguyên dành cho Claude (Skills, MCP, Agent) trên Mac với giao diện đồ họa tiện lợi.

4. [TrustClaw](https://www.trustclaw.app/)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032305.webp)

Một phiên bản tinh chỉnh của OpenClaw nhằm tăng cường bảo mật và giảm thiểu các rủi ro từ mã nguồn gốc.

## Tài nguyên

1. [Project N.O.M.A.D.](https://github.com/Crosstalk-Solutions/project-nomad)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032302.webp)

Một kho tri thức khổng lồ được nén vào ứng dụng Linux để bạn có thể tra cứu Wikipedia, bản đồ hay học tập ngay cả khi không có internet.

2. [AI Coding Agent cho phân tích dữ liệu](https://simonw.github.io/nicar-2026-coding-agents/index.html) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032204.webp)

Tài liệu hướng dẫn chi tiết cách dùng AI để thực hiện các bước phân tích dữ liệu chuyên nghiệp từ chuyên gia Simon Willison.

3. [TypeScript Concise Book](https://gibbok.github.io/typescript-book/zh-cn/book/the-concise-typescript-book/)

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011203.webp)

Cuốn sách hướng dẫn TypeScript súc tích và dễ hiểu, đã có bản dịch tiếng Trung.

## Hình ảnh

1. [Trứng phục sinh (Easter Egg) trong hình nền Apple](https://www.macworld.com/article/3079526/easter-egg-hiding-in-macbook-neos-wallpaper.html)

Apple luôn biết cách tạo bất ngờ. Trong hình nền của MacBook Neo mới, họ đã khéo léo lồng ghép tên sản phẩm vào các họa tiết. Thực tế đây là truyền thống của họ từ lâu.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032502.webp)

iMac

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032503.webp)

MacBook Pro

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032504.webp)

iPad Air

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032505.webp)

MacBook Air

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032507.webp)

iPad Mini

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032506.webp)

iPad Pro

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032508.webp)

2. [Tỷ lệ tử vong ở trẻ em](https://kottke.org/25/12/an-astonishing-graph)

Một sự thật khó tin: trong phần lớn lịch sử loài người, tỷ lệ trẻ em không sống sót đến tuổi trưởng thành từng lên tới gần 50%. Chỉ từ cuối thế kỷ 19, con số này mới bắt đầu giảm mạnh nhờ y học hiện đại.

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120307.webp)

## Điểm tin

1. [Đừng biến mình thành cỗ máy](https://blog.armeet.ca/becoming-the-machine/)

"Chỉ những kẻ nô lệ mới định lượng giá trị bản thân bằng năng suất". Câu nói này khiến tôi phải suy ngẫm về "văn hóa cày cuốc" trên mạng xã hội hiện nay. Mọi người tự hào về việc dậy lúc 5 giờ sáng hay là người cuối cùng rời văn phòng. Nhưng đó chẳng phải là đang cố biến mình thành một cỗ máy sao? Máy móc tuy hiệu quả nhưng lại cứng nhắc. Con người chúng ta nên quý trọng sự linh hoạt và khả năng thích nghi nhanh chóng, thay vì chỉ chăm chăm vào những công việc lặp đi lặp lại một cách vô hồn.

## Phát ngôn

1.

Chúng ta đã tạo ra một nền văn minh phụ thuộc sâu sắc vào khoa học kỹ thuật, nhưng lại để cho đa số mọi người không thấu hiểu chúng. Đây là một sự kết hợp nguy hiểm giữa sự thiếu hiểu biết và quyền lực, sớm muộn gì nó cũng sẽ bùng nổ.

-- Carl Sagan.

2.

Paris từng là nỗi ám ảnh về tắc đường. Thị trưởng thành phố đã quyết định cắt giảm mạnh số lượng chỗ đậu xe, và kết quả là người dân đã thực sự ít lái xe hơn.

-- CNN.

3.

Một nghiên cứu chỉ ra rằng khi học trực tuyến, những sinh viên có ngoại hình ưa nhìn thường có kết quả bài tập thấp hơn so với khi học trực tiếp tại lớp.

-- Economics Letters.

4.

Thay đổi lớn nhất của tôi trong những năm qua là thói quen sống vào ban ngày. Việc thức dậy sớm để đón bình minh giúp tâm hồn tôi cảm thấy bình an và nhịp sống hài hòa hơn với thiên nhiên.

-- Herman's Bear Blog.

5.

AI cực kỳ giỏi trong việc biến những ý tưởng rõ ràng thành mã nguồn chạy được. Cái khó nhất và tốn thời gian nhất vẫn là xác định xem tôi thực sự muốn xây dựng cái gì.

-- lustin.fr.

## Nhìn lại các năm trước

[Cách ngăn chặn AI bò lướt dữ liệu](https://www.ruanyifeng.com/blog/2025/03/weekly-issue-343.html) (#343)

[Một tuần chiếm 2% của một năm](https://www.ruanyifeng.com/blog/2024/03/weekly-issue-293.html) (#293)

[Trò chuyện với AI Khổng Tử](https://www.ruanyifeng.com/blog/2023/02/weekly-issue-243.html) (#243)

[Frontend và Backend, bên nào khó hơn?](https://www.ruanyifeng.com/blog/2022/01/weekly-issue-193.html) (#193)

(Hết)
