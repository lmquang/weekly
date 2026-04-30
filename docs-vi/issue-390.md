# Thiếu dữ liệu, AI chỉ là một kẻ khờ

Bản tin này ghi lại những nội dung công nghệ đáng chia sẻ hàng tuần, phát hành vào thứ Sáu.

Tạp chí này [mã nguồn mở](https://github.com/ruanyf/weekly), hoan nghênh bạn [đóng góp](https://github.com/ruanyf/weekly/issues). Ngoài ra còn có dịch vụ ["Ai đang tuyển dụng"](https://github.com/ruanyf/weekly/issues/9088) dành cho các lập trình viên. Nếu muốn hợp tác, bạn hãy [liên hệ qua email](mailto:yifeng.ruan@gmail.com) (yifeng.ruan@gmail.com) nhé.

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032201.webp)

Một hành lang đầy màu sắc tại một khu dân cư ở Nhật Chiếu, Sơn Đông. Đặc biệt, lối vào hành lang xuyên qua một lùm cây còn có cả quán cà phê cực chill. ([via](https://mooool.com/coffee-tree-canopy-by-selgascano.html))

## Thiếu dữ liệu, AI chỉ là một kẻ khờ

Nếu bây giờ làm một cuộc khảo sát với câu hỏi: "Bạn có nghĩ mô hình lớn (LLM) thực sự có trí thông minh?", tôi tin phần lớn câu trả lời sẽ là "Có".

Dù mới ở giai đoạn sơ khai, AI đã thay thế được rất nhiều công việc trí óc của con người, điều đó thực sự kỳ diệu. Thế nhưng, chúng ta đừng quên một thực tế: **AI không phải là phép màu, càng không phải một thực thể có trí tuệ tự thân. Nó là một mô hình ngôn ngữ dựa trên các quy luật thống kê**. Mọi hành vi của nó đều bắt nguồn từ các phép toán xác suất.

Minh chứng rõ nhất là nếu bạn đưa cho nó một bài toán mà nó chưa từng được huấn luyện, tức là không tồn tại quy luật thống kê nào trong kho dữ liệu của nó, AI sẽ hoàn toàn bó tay.

Tôi muốn chia sẻ với bạn về một [thí nghiệm](https://esolang-bench.vercel.app/) thú vị gần đây.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032008.webp)

Hai nhà nghiên cứu đã chọn ra 5 gương mặt đình đám nhất làng AI hiện nay: GPT-5.2, O4-mini, Gemini 3 Pro, Qwen3-235B và Kimi K2. Nhiệm vụ của chúng là sử dụng 5 ngôn ngữ lập trình "siêu hiếm" (Esoteric languages) gồm Brainfuck, Befunge-98, Whitespace, Unlambda và Shakespeare để giải quyết các bài toán.

Đặc điểm chung của những ngôn ngữ này là tài liệu trên mạng cực kỳ ít, đồng nghĩa với việc AI có rất ít dữ liệu để học. Kết quả thế nào bạn đoán được không?

Tóm gọn trong một câu: Thất bại thảm hại.

Tỷ lệ giải bài đúng trung bình của cả 5 mô hình này chỉ vỏn vẹn 3,8%. Nghĩa là **giải 100 bài thì chỉ đúng được chưa tới 4 bài**. Để so sánh, khi giải toán bằng Python, tỷ lệ chính xác của chúng có thể lên tới 94%.

Trớ trêu hơn, vài bài toán hiếm hoi mà chúng giải đúng đều nằm ở mức "vỡ lòng". Còn với các mức độ khó hơn (sơ cấp, trung cấp, cao cấp), cả 5 "ông lớn" này đều đồng loạt nhận điểm 0 tròn trĩnh.

Thí nghiệm này cho thấy một chân lý: **Sức mạnh (hay trí thông minh) của AI hoàn toàn bị chi phối bởi dữ liệu huấn luyện**. Dữ liệu càng nhiều, AI càng thông minh. Python có mặt ở khắp mọi nơi nên AI cực giỏi Python. Dữ liệu càng ít, AI càng ngây ngô và gần như vô dụng.

Vậy có một câu hỏi khá thú vị đặt ra: Nếu một ngôn ngữ hiếm không có dữ liệu huấn luyện, nhưng chúng ta ném cho AI một cuốn "Cẩm nang sử dụng" thật chi tiết, liệu nó có thể tự học để lập trình được không?

## MAI-Image-2

Tuần này, Microsoft vừa trình làng mô hình tạo ảnh [MAI-Image-2](https://microsoft.ai/news/introducing-MAI-Image-2/).

Nhiều [đánh giá](https://decrypt.co/361791/microsoft-mai-image-2-text-image-model-review) cho rằng chất lượng ảnh của nó cực kỳ ấn tượng, hiện chỉ đứng sau Nano Banana 2 của Google. Bạn có thể dùng thử miễn phí tại [MAI Playground](https://playground.microsoft.ai/chat).

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032009.webp)

Tôi đã thử và thấy độ chân thực của ảnh rất tốt. Ví dụ, đây là ảnh "một chú chó đang đạp xe dưới biển".

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032010.webp)

Tuy nhiên, rào cản sử dụng của nó vẫn còn khá nhiều: (1) Từ chối tạo các ảnh nhạy cảm hoặc gây tranh cãi; (2) Giới hạn 15 ảnh mỗi ngày, mỗi lần cách nhau 30 giây; (3) Chỉ hỗ trợ tỷ lệ 1:1; (4) Không có công cụ chỉnh sửa, chỉ thuần túy là tạo ảnh từ văn bản.

Dù vậy, nếu bạn cần một bức ảnh chất lượng cao và chân thực, đây vẫn là một lựa chọn rất đáng thử.

## Tin công nghệ

1. [Tờ bìa có thể chơi game](https://www.yankodesign.com/2026/03/16/red-bull-just-put-a-playable-tetris-game-on-a-magazine-cover/)

Red Bull vừa tung ra tạp chí game mang tên *GamePop*. Điều đặc biệt nằm ở chỗ tờ bìa của nó tích hợp sẵn trò xếp gạch Tetris có thể chơi được.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032003.webp)

Bí mật nằm ở một bảng mạch linh hoạt siêu mỏng được nhúng ngay trong tờ bìa, bao gồm 180 đèn LED RGB, 7 nút cảm ứng và một con chip ARM 32-bit. Thậm chí nó còn có cả pin sạc qua cổng Type-C. Đáng tiếc là đây là phiên bản giới hạn, chỉ có 150 bản trên toàn thế giới.

2. [Chờ 15 phút để gặp người thật](https://arstechnica.com/gadgets/2025/02/misguided-hp-customer-support-approach-included-forced-15-minute-call-wait-times/)

Các doanh nghiệp ngày càng ngại cung cấp dịch vụ hỗ trợ qua điện thoại có người thật vì chi phí đắt đỏ. HP vừa nghĩ ra một chiêu để "lùa" khách hàng sang dùng chatbot: nếu bạn khăng khăng đòi gặp nhân viên hỗ trợ, hệ thống sẽ bắt bạn chờ đúng 15 phút mới kết nối. Đây có lẽ sẽ là tương lai: hỗ trợ miễn phí thì dùng AI, muốn gặp người thật thì phải trả thêm phí hoặc kiên nhẫn chờ đợi.

3. [Vật lý học và môn ném đĩa](https://arstechnica.com/science/2024/10/how-physics-can-improve-your-disc-golf-game/)

Làm sao để ném đĩa vừa nhanh vừa xa? Một nhà vật lý học tại Mỹ đã làm thí nghiệm và phát hiện ra rằng: đặt ngón tay cái cách mép đĩa khoảng 3cm sẽ cho kết quả tối ưu nhất về cả tốc độ xoáy lẫn vận tốc ban đầu. Tốc độ xoáy càng cao thì đĩa bay càng nhanh.

## Bài viết hay

1. [Sự sụp đổ âm thầm của MkDocs](https://fpgmaas.com/blog/collapse-of-mkdocs/) (Tiếng Anh)

MkDocs vốn là công cụ tạo trang tài liệu rất nổi tiếng, nhưng những mâu thuẫn gay gắt giữa các thành viên chủ chốt đang khiến dự án này dần tan rã.

2. [Dùng AI dự đoán tốc độ hạ nhiệt của cà phê](https://dynomight.net/coffee/) (Tiếng Anh)

Tác giả yêu cầu các mô hình AI đưa ra công thức tính toán thời gian nguội đi của ly cà phê, sau đó đối chiếu với kết quả thực tế để tìm ra mô hình thông minh nhất.

3. [Tương lai của App có thể là "vô diện"](https://tuananh.net/2026/03/18/why-your-next-mobile-app-is-probably-headless/) (Tiếng Anh)

Nếu sau này chúng ta chủ yếu dùng điện thoại qua trợ lý AI, thì các ứng dụng sẽ không cần giao diện đồ họa nữa. Chúng chỉ cần cung cấp các cổng dữ liệu (API) để AI tự điều phối.

4. [Nén dữ liệu ngay trên trình duyệt](https://jstrieb.github.io/posts/canvas-compress/) (Tiếng Anh)

Một mẹo nhỏ để nén dữ liệu thành một bức ảnh thông qua thẻ canvas của HTML5 ngay tại phía Frontend.

5. [Ruby là ngôn ngữ tốt nhất cho AI](https://paolino.me/ruby-is-the-best-language-for-ai-apps/) (Tiếng Anh)

Tác giả đã so sánh Python, JavaScript và Ruby khi xây dựng một AI Agent và kết luận rằng Ruby mang lại trải nghiệm phát triển mượt mà nhất.

## Công cụ

1. [proxychains-rs](https://github.com/tianrking/proxychains-rs)

Phiên bản Rust của proxychains4, giúp điều hướng lưu lượng của một tiến trình cụ thể qua chuỗi proxy. ([@tianrking](https://github.com/ruanyf/weekly/issues/9316) đóng góp)

2. [Flare Stack Blog](https://github.com/du2333/flare-stack-blog)

Hệ thống blog chạy hoàn toàn trên hạ tầng của Cloudflare (D1, R2, KV). ([@du2333](https://github.com/ruanyf/weekly/issues/9312) đóng góp)

3. [Tunelo](https://github.com/jiweiyuan/tunelo)

Công cụ giúp public dịch vụ từ local ra internet cực nhanh qua giao thức QUIC, chỉ với một file thực thi duy nhất. ([@jiweiyuan](https://github.com/ruanyf/weekly/issues/9328) đóng góp)

4. [ReadAny](https://github.com/codedogQBY/ReadAny)

Ứng dụng đọc ebook đa nền tảng tích hợp AI và khả năng đồng bộ dữ liệu. ([@codedogQBY](https://github.com/ruanyf/weekly/issues/9342) đóng góp)

5. [Work Review](https://github.com/wm94i/Work_Review)

Ứng dụng ghi lại toàn bộ lịch sử sử dụng phần mềm và website trong ngày để bạn dễ dàng tổng kết công việc. ([@wm94i](https://github.com/ruanyf/weekly/issues/9382) đóng góp)

6. [Chokidar](https://github.com/paulmillr/chokidar)

Một module Node.js mạnh mẽ hơn hẳn fs.watch gốc để theo dõi mọi biến động của hệ thống tập tin.

## AI liên quan

1. **Giao diện WeChat cho AI**

Tuần này WeChat vừa tung ra cổng kết nối cho phép các chatbot AI gửi tin nhắn trực tiếp vào ứng dụng. Cộng đồng đã nhanh chóng có các bộ SDK hỗ trợ:
- [wechat-rs-sdk](https://github.com/tianrking/weixin-agent-rs) (Rust)
- [WeChatBot](https://github.com/corespeed-io/wechatbot) (Go)
- [WeClaw](https://github.com/fastclaw-ai/weclaw) (Python)

2. [AI CLI Complete Notify](https://github.com/ZekerTop/ai-cli-complete-notify)

Nhận thông báo qua Telegram hoặc Webhook ngay khi các tác vụ dòng lệnh của AI (như Claude Code) hoàn thành. ([@ZekerTop](https://github.com/ruanyf/weekly/issues/9348) đóng góp)

3. [Claude Config Manager](https://github.com/Daydayoneup/ccm)

Giao diện đồ họa giúp bạn quản lý các Skill, MCP và Agent của Claude một cách trực quan trên Mac. ([@Daydayoneup](https://github.com/ruanyf/weekly/issues/9370) đóng góp)

## Hình ảnh

1. [Bí mật trong hình nền của Apple](https://www.macworld.com/article/3079526/easter-egg-hiding-in-macbook-neos-wallpaper.html)

Apple luôn giấu những "quả trứng phục sinh" trong hình nền của các dòng máy mới. Nếu soi kỹ, bạn sẽ thấy tên của sản phẩm được cách điệu một cách cực kỳ tinh tế ngay trong các đường nét của hình nền. Từ MacBook Neo, iMac cho đến iPad Pro đều có chi tiết thú vị này.

2. [Tỷ lệ tử vong ở trẻ em](https://kottke.org/25/12/an-astonishing-graph)

Ít ai biết rằng trong phần lớn lịch sử nhân loại, tỷ lệ tử vong ở trẻ em (trước tuổi trưởng thành) luôn ở mức xấp xỉ 50%. Phải đến cuối thế kỷ 19, con số này mới bắt đầu giảm mạnh nhờ những tiến bộ y tế. Đến năm 2020, tỷ lệ này trung bình toàn cầu chỉ còn 4,3%.

## Văn trích

1. [Đừng biến mình thành máy móc](https://blog.armeet.ca/becoming-the-machine/)

Tôi vừa đọc được một câu nói rất hay: "Chỉ có nô lệ mới dùng năng suất để định nghĩa giá trị tồn tại của chính mình". Thời đại nay chúng ta hay bị ám ảnh bởi việc phải trở nên cực kỳ năng suất, phải dậy từ 5 giờ sáng, phải là người cuối cùng rời văn phòng. Đó thực chất là việc cố gắng bắt chước máy móc. Nhưng bạn là con người, thế mạnh của bạn là sự linh hoạt và khả năng ứng biến. Đừng đâm đầu vào những công việc lặp đi lặp lại một cách mù quáng, hãy tập trung tìm ra những giải pháp thực sự có giá trị.

## Trích dẫn

1.

Chúng ta đang xây dựng một nền văn minh dựa hoàn toàn vào khoa học công nghệ, nhưng lại khiến những thứ đó trở nên quá khó hiểu với số đông. Đây là một sự kết hợp nguy hiểm và sớm muộn gì nó cũng sẽ phát nổ.

-- Carl Sagan

2.

Paris từng rất tắc đường, nhưng khi thị trưởng quyết định xóa bỏ hàng loạt bãi đỗ xe, người dân bỗng dưng lười lái xe hẳn đi.

-- CNN

3.

Nghiên cứu cho thấy khi học online, những sinh viên có ngoại hình ưu tú thường nhận được điểm số thấp hơn so với khi học trực tiếp.

-- Economics Letters

4.

Thay đổi lớn nhất của đời tôi là chuyển từ một "cú đêm" sang một người yêu buổi sáng. Việc được tận mắt ngắm nhìn bình minh và hoàng mỗi ngày giúp tôi cảm thấy bình an và nhịp sống của mình hòa quyện hơn với thiên nhiên.

-- Becoming a Day Person

5.

AI cực giỏi trong việc biến những ý tưởng rõ ràng thành mã nguồn chạy được. Việc tốn thời gian nhất bây giờ là ngồi nghĩ xem mình thực sự muốn xây dựng cái gì.

-- lustin.fr

## Nhìn lại năm xưa

[Cách chặn bot AI cào dữ liệu](https://www.ruanyifeng.com/blog/2025/03/weekly-issue-343.html) (#343)

[Một tuần chỉ chiếm 2% của một năm](https://www.ruanyifeng.com/blog/2024/03/weekly-issue-293.html) (#293)

[Trò chuyện cùng Khổng Tử AI](https://www.ruanyifeng.com/blog/2023/02/weekly-issue-243.html) (#243)

[Frontend và Backend, bên nào khó hơn?](https://www.ruanyifeng.com/blog/2022/01/weekly-issue-193.html) (#193)

(Hết)
