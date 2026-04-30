# Bạn đang thuộc nhóm dẫn đầu

Đây là nơi ghi lại những nội dung công nghệ đáng chia sẻ hàng tuần, xuất bản vào mỗi thứ Sáu.

Tạp chí này [nguồn mở](https://github.com/ruanyf/weekly), rất hoan nghênh các bạn [đóng góp nội dung](https://github.com/ruanyf/weekly/issues). Ngoài ra còn có dịch vụ ["Ai đang tuyển dụng"](https://github.com/ruanyf/weekly/issues/9088), nơi đăng tải thông tin tuyển dụng lập trình viên. Để hợp tác, vui lòng [liên hệ qua email](mailto:yifeng.ruan@gmail.com) (yifeng.ruan@gmail.com).

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030503.webp)

Đèn lồng Cá Phúc tại lễ hội hoa đăng Tết Nguyên tiêu ở Phúc Châu. Một thiết bị cơ khí dài 25 mét đang lơ lửng trên không trung. ([via](http://fj.people.com.cn/n2/2026/0304/c181466-41515232.html))

## Bạn đang thuộc nhóm dẫn đầu

Dân số thế giới hiện nay là 8,1 tỷ người. Nếu chúng ta vẽ một [biểu đồ ô vuông](https://www.reddit.com/r/vibecoding/comments/1rbqldk/youre_early/), với mỗi ô đại diện cho 3,2 triệu người, bức tranh sẽ trông như thế này:

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022615.webp)

- 6,88 tỷ người (84%) chưa từng chạm tay vào AI (ô màu xám).
- 1,38 tỷ người (16%) đã từng trò chuyện với AI (ô màu xanh lá).
- 15 - 25 triệu người (0,3%) đang trả phí cho các dịch vụ AI (ô màu vàng).
- 2 - 5 triệu người (0,04%) đã dùng AI để tự tạo ra các dự án lập trình của riêng mình (ô màu đỏ).

Nếu bạn đang đọc bản tin này, quan tâm đến các chuyển động của AI và từng dùng AI để sinh mã nguồn, bạn đã thực sự dẫn đầu 99% dân số thế giới rồi đấy.

## Sự an toàn của OpenClaw

Hiện tại, phần mềm "nóng" nhất thế giới chắc chắn là trợ lý AI cá nhân [OpenClaw](https://openclaw.ai/).

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030302.webp)

Độ nóng của nó khủng khiếp đến mức nào? Trong vòng 4 tháng, nó đã đạt được 250.000 sao trên GitHub, vượt qua cả React để trở thành [dự án phần mềm có nhiều sao nhất lịch sử](https://www.star-history.com/blog/openclaw-surpasses-react-most-starred-software).

Hãy nhớ rằng React mất 13 năm để đạt 250.000 sao đó, còn OpenClaw chỉ cần 4 tháng.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030303.webp)

Trong biểu đồ trên, đường màu đỏ dựng đứng chính là OpenClaw. Quá ấn tượng.

Vai trò của OpenClaw là giúp bạn điều khiển máy tính thông qua ngôn ngữ tự nhiên để hoàn thành các tác vụ tự động. Trước đây, bạn cần rất nhiều công cụ và kỹ năng chuyên môn mới làm được điều tương tự. Giờ đây, chỉ cần nhập văn bản hoặc ra lệnh bằng giọng nói. Nó không chỉ hữu ích mà còn rất thú vị.

Về cơ bản, nó chính là những gì mà Siri của Apple nên trở thành. Với người dùng phổ thông, đây mới là cách tương tác đúng đắn với máy tính. Có thể dự đoán trong vài năm tới, những công cụ loại này sẽ phổ cập đến điện thoại của mọi người.

Nhưng có một vấn đề: nó chưa đủ an toàn.

OpenClaw có hơn 400.000 dòng mã, 53 tệp cấu hình và hơn 70 thư viện phụ thuộc, tất cả được AI tạo ra chỉ trong vài tuần mà không qua bất kỳ quy trình kiểm duyệt chính thống nào. Nó đòi hỏi quyền truy cập vào các khóa cá nhân của bạn với đặc quyền cực lớn và chạy hoàn toàn tự động. Nhiều người đã cấp quyền cho nó truy cập cả Apple ID hay Gmail, thật khó tưởng tượng hậu quả nếu xảy ra lỗi.

Các biện pháp bảo vệ của nó rất sơ sài, và do thiết kế ban đầu, nó rất dễ bị lộ lên mạng công cộng nếu người dùng không cẩn thận.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030301.webp)

Đã có người tạo ra một [Bảng theo dõi mức độ phơi nhiễm OpenClaw](https://openclaw.allegro.earth/) để thu thập tất cả các phiên bản OpenClaw đang bị lộ lên internet. Bạn có biết con số hiện tại là bao nhiêu không? Tính đến hôm qua là 258.305.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030304.webp)

Chỉ cần chọn đại một máy và nhấn vào, bạn sẽ thấy ngay bảng điều khiển của họ. Những người đó cứ ngỡ mình đang tự động hóa máy tính cá nhân, nhưng không ngờ họ đang mở toang cửa cho cả thế giới. Nếu bạn định dùng OpenClaw, ít nhất hãy cài nó trên một máy ảo hoặc máy vật lý riêng biệt, bằng không thì chỉ còn biết trông chờ vào vận may thôi.

## Tin công nghệ

1. [Băng giấy mã QR](https://www.theresistornetwork.com/2021/03/qrtape-audio-playback-from-paper-tape.html)

Một nhà sáng chế nước ngoài nảy ra ý tưởng kỳ lạ: liệu có thể lưu trữ âm thanh trên băng giấy không?

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022303.webp)

Ông đã mã hóa âm thanh của mỗi giây thành một mã QR và in chúng lần lượt lên một dải giấy dài.

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022304.webp)

Ông cũng chế tạo luôn một máy phát nhạc với vỏ bằng bìa các-tông, bên trong có bộ truyền động và camera.

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022305.webp)

Máy phát sẽ kéo băng giấy đi qua mỗi giây một ô, camera nhận diện dữ liệu từ mã QR và khôi phục lại thành âm thanh để phát ra loa.

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022306.webp)

2. [Chính phủ Hàn Quốc làm mất tiền điện tử](https://www.bleepingcomputer.com/news/security/48m-in-crypto-stolen-after-korean-tax-agency-exposes-wallet-seed/)

Cục Thuế Quốc gia Hàn Quốc đã tịch thu một lượng lớn tiền điện tử từ những kẻ trốn thuế. Sau đó, cơ quan thực thi pháp luật đã công bố ảnh chụp "chiến lợi phẩm" lên mạng.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030202.webp)

Bức ảnh có độ phân giải cao, chụp một chiếc ví lạnh cùng một tờ giấy ghi tay mã khóa khôi phục (seed phrase). Kết quả là toàn bộ số tiền trị giá 4,4 triệu USD đã bị kẻ gian tẩu tán ngay lập tức. Vụ việc cho thấy rủi ro cực lớn khi chính phủ nắm giữ tiền điện tử mà không có quy trình bảo mật nghiêm ngặt.

3. [Cách đi của khủng long bạo chúa T-Rex](https://phys.org/news/2026-02-flatfooted-lumbering-rex-tiptoes.html)

T-Rex là loài khủng long khổng lồ hung hãn, vua của kỷ Phấn trắng.

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022803.webp)

Vẫn còn nhiều bí ẩn quanh loài vật này, chẳng hạn như tại sao chi trước của chúng lại ngắn và nhỏ đến vậy. Gần đây, các nhà khoa học lại phát hiện thêm một đặc điểm nữa: loài vật to xác này hóa ra lại đi bằng... nhón chân.

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022804.webp)

Các hóa thạch dấu chân cho thấy vết hằn ở phần ngón chân là sâu nhất, chứng tỏ đây là nơi chịu lực chính.

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022805.webp)

Việc đi bằng nhón chân có thể giúp T-Rex tăng tốc độ, mang lại lợi thế lớn khi săn mồi.

## Bài viết

1. [Một kỹ thuật để tăng cường sức mạnh mô hình AI](https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022702.webp)

Khi AI không biết làm hoặc làm chưa tốt một việc gì đó, developer nổi tiếng Simon Willison gợi ý một cách giải quyết: bạn hãy tìm những bài viết hướng dẫn hoặc ví dụ mã nguồn chạy được về mảng đó rồi đưa vào ngữ cảnh (context) cho mô hình tham khảo. AI sẽ học cách giải quyết vấn đề dựa trên các ví dụ đó. Vậy nên, hãy "tích trữ" những gì bạn biết cách làm để AI có thể thay bạn thực hiện chúng sau này.

2. [Tôi đã tạo ra một phiên bản AI của chính mình](https://luolei.org/luolei-ai) (Tiếng Trung)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030307.webp)

Tác giả chia sẻ cách huấn luyện một phiên bản kỹ thuật số từ các dữ liệu blog, video và mạng xã hội suốt hơn mười năm của mình để tạo ra một "phân thân" có thể trò chuyện trực tuyến với mọi người.

3. [Lưu ý về lệnh scp](https://sny.sh/hypha/blog/scp) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022802.webp)

Lệnh `scp` thường dùng để truyền tệp lên máy chủ. Tuy nhiên, nó sao chép cả quyền hạn của tệp và trong một số trường hợp, nó có thể vô tình vô hiệu hóa quyền truy cập SSH vào máy chủ.

4. [So sánh Nano Banana 2 và Seedream 5.0 Lite](https://decrypt.co/359700/image-ai-leap-google-bytedances-latest-models) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030405.webp)

So sánh hai mô hình tạo ảnh tiên tiến nhất hiện nay từ Google và ByteDance để xem ai vượt trội hơn.

5. [Bốn cách duyệt mảng trong JavaScript](https://waspdev.com/articles/2026-01-01/javascript-for-of-loops-are-actually-fast#javascript_s_for_of_loops_are_actually_fast) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011012.webp)

Bài viết kết luận rằng vòng lặp `for i++` truyền thống có tốc độ nhanh nhất, tiếp theo là `for-of`, `forEach` chậm hơn, và nên tránh sử dụng `for-in` để duyệt mảng.

## Công cụ

1. [yj_nearbyglasses](https://github.com/yjeanrenaud/yj_nearbyglasses)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030402.webp)

Ứng dụng Android nguồn mở giúp bạn kiểm tra xem xung quanh có cặp kính thông minh nào đang hoạt động không.

2. [explain-my-curl](https://github.com/akgitrepos/explain-my-curl)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030403.webp)

Giao diện dòng lệnh giúp giải thích kết quả thực thi của các lệnh `curl`.

3. [Pocket ID](https://github.com/pocket-id/pocket-id)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030501.webp)

Dịch vụ xác thực OIDC mà bạn có thể tự triển khai, hỗ trợ đăng nhập không mật khẩu qua Passkey.

4. [R2 Web](https://github.com/vikiboss/r2-web)

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022703.webp)

Trình quản lý tệp trên nền web cho dịch vụ lưu trữ Cloudflare R2.

5. [Voxt](https://github.com/hehehai/voxt)

Ứng dụng macOS dùng để chuyển giọng nói thành văn bản và dịch thuật trực tiếp theo thời gian thực.

6. [Cutia](https://github.com/msgbyte/cutia)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030103.webp)

Trình chỉnh sửa video trực tuyến nguồn mở, một lựa chọn thay thế cho CapCut trên trình duyệt.

7. [Gorse](https://github.com/gorse-io/gorse)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030201.webp)

Hệ thống gợi ý nguồn mở giúp tự động huấn luyện dữ liệu và tạo ra các nội dung đề xuất cá nhân hóa cho người dùng.

8. [vscode-stylelint-plus](https://github.com/hex-ci/vscode-stylelint-plus)

Tiện ích mở rộng cho VSCode để kiểm tra lỗi cú pháp và định dạng cho CSS, SCSS, Less.

9. [OneDroid](https://qingge.tech/onedroid/web/)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030401.webp)

Ứng dụng Android nguồn mở cung cấp nhiều công cụ tiện ích để quản lý thiết bị của bạn.

10. [NoteCalc](https://github.com/2234839/TsFullStack)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030502.webp)

Sổ tay tính toán thời gian thực với phong cách "nhìn là thấy ngay kết quả".

## AI

1. [no-agents.md](https://codeberg.org/rossabaker/no-agents.md)

Nếu không muốn kho mã nguồn của mình bị các mô hình AI thu thập để huấn luyện, bạn có thể thêm các tệp `AGENTS.md` và `CLAUDE.md` từ dự án này vào repo của mình.

2. [Skills Manager](https://github.com/xingkongliang/skills-manager)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030207.webp)

Ứng dụng macOS giúp quản lý tập trung các tệp Skill và đồng bộ chúng đến các công cụ AI khác nhau.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030406.webp)

Cũng có một dự án khác cùng tên [Skills Manager](https://github.com/Rito-w/skills-manager) với tính năng tương tự.

3. [AGI Agent](https://github.com/agi-hub/AGIAgent)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030306.webp)

Trợ lý AI cá nhân nguồn mở, một sự thay thế cho OpenClaw với khả năng tương thích tốt với các mô hình AI nội địa.

4. [ArXiv Daily Researcher](https://github.com/yzr278892/arxiv-daily-researcher)

Ứng dụng Python giúp tự động cập nhật và lọc các bài báo khoa học mới nhất từ ArXiv dựa trên từ khóa tùy chỉnh.

5. [Magic Resume (Ma phương sơ yếu lý lịch)](https://github.com/JOYCEQL/magic-resume)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030206.webp)

Trình biên tập hồ sơ trực tuyến tích hợp các năng lực từ AI để tối ưu nội dung.

## Tài nguyên

1. [Giải thích tương tác về MicroGPT](https://growingswe.com/blog/microgpt) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030203.webp)

MicroGPT là một đoạn mã Python dài 200 dòng dùng để giải thích nguyên lý hoạt động của ChatGPT. Bài viết sử dụng các hoạt ảnh tương tác để giúp người mới bắt đầu dễ dàng hiểu về thuật toán của các mô hình ngôn ngữ lớn.

2. [Dự báo mùa hoa anh đào 2026 tại Trung Quốc](https://rogerzhu.github.io/yinghua-map/)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030305.webp)

Bản đồ dự báo ngày hoa anh đào nở rộ tại các địa phương.

3. [Now I Get It!](https://nowigetit.us/)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030101.webp)

Tải lên tệp PDF của một bài báo khoa học, trang web này sẽ chuyển nó thành một trang web tương tác giải thích nội dung bằng tiếng Anh đơn giản.

## Hình ảnh

1. [Quảng cáo Apple sau 30 năm](https://www.instagram.com/p/DHUbY9aSqK5/)

Quảng cáo năm 1997 của Apple với nhân vật chính là Einstein.

![](https://cdn.beekka.com/blogimg/asset/202503/bg2025032011.webp)

Và quảng cáo năm 2025 với nhân vật chính là một chú ếch.

![](https://cdn.beekka.com/blogimg/asset/202503/bg2025032012.webp)

Thật khó tưởng tượng ngày nay Apple lại dùng Einstein để làm quảng cáo. So với thế kỷ trước, xã hội loài người đã trở nên "giải trí" hơn rất nhiều, bớt đi sự nghiêm túc và đạo mạo.

## Điểm tin

1. [Tôi bị sa thải qua WhatsApp khi sếp đang đi nghỉ mát](https://ginoz.bearblog.dev/my-boss-fired-me-over-whatsapp-while-he-was-on-vacation-in-honolulu/)

Tôi làm việc cho một công ty tư nhân nhỏ. Cách đây ít lâu, tôi đã hoàn thành hết mọi việc và ngồi chơi xơi nước suốt hai tuần vì quản lý không giao việc mới. Tôi cảm thấy có gì đó không ổn nên đã nhắn tin hỏi sếp qua Slack.

Nhiều giờ rồi nhiều ngày trôi qua vẫn không có hồi âm. Cuối cùng tôi nhắn qua WhatsApp cá nhân của ông. Ông trả lời rằng mình đang nghỉ mát ở Hawaii và không xem Slack. Sau đó là một tin nhắn dài dằng dặc thông báo tôi đã bị sa thải. Lý do là công ty đang thua lỗ và cắt giảm nhân sự là cách duy nhất để sống sót.

Tôi đã rất sốc. Tôi từng làm việc cho ông suốt 4 năm, vậy mà ông sa thải tôi bằng một tin nhắn văn bản khi đang đi nghỉ mát, thậm chí không đủ can đảm để thực hiện một cuộc gọi video hay gặp mặt trực tiếp. Tôi chợt nhận ra mình làm việc cực khổ chỉ để đóng góp vào hạnh phúc và sự giàu sang của ông, còn ông thì chẳng cần chút lòng trắc ẩn hay sự dũng cảm tối thiểu nào khi đối diện với tôi.

## Phát ngôn

1.

Điều khiến tôi ngạc nhiên là gần đây mọi người bắt đầu làm những việc đáng lẽ phải làm từ lâu: (1) Viết tài liệu ngắn gọn, trực diện trong tệp AGENTS.md. (2) Hiện thực hóa các quy trình công việc giá trị dưới dạng Skill hoặc máy chủ MCP. (3) Cải thiện đầu ra của các công cụ dòng lệnh để chúng mang lại nhiều thông tin hữu ích hơn cho AI.

-- [《AI=true là một phản mô hình》](https://keleshev.com/ai-equals-true-is-an-anti-pattern)

2.

GitHub gần đây hay bị sập, tôi nghĩ lý do không phải vì họ đang chạy mã do AI tạo ra, mà vì người dùng đang đẩy lên quá nhiều mã do AI sinh ra với tần suất và số lượng vượt xa trước đây, khiến hệ thống quá tải.

-- Độc giả trên Hacker News.

3.

GitHub Star từng là một chỉ số rất tốt, cho đến khi mọi người dần nhận ra rằng nó thực sự là một chỉ số... quá tốt (nên bị thao túng).

-- Độc giả trên Hacker News.

4.

Với AI, một kỹ sư có thể hoàn thành bảy tính năng chỉ trong một chu kỳ phát triển, việc thăng tiến bỗng trở nên quá dễ dàng.

-- [《Khi tốc độ sinh mã vượt xa khả năng thấu hiểu》](https://www.rockoder.com/beyondthecode/cognitive-debt-when-velocity-exceeds-comprehension/)

5.

Chỉ có một cách duy nhất để ăn hết một con voi: đó là ăn từng miếng một.

-- Giám mục Desmond Tutu.

## Nhìn lại các năm trước

[Ba mươi năm thổi phồng công nghệ](https://www.ruanyifeng.com/blog/2025/03/weekly-issue-340.html) (#340)

[Vấn đề lớn nhất của kính Vision Pro](https://www.ruanyifeng.com/blog/2024/02/weekly-issue-290.html) (#290)

[Có thể rút ngắn thời gian giáo dục không?](https://www.ruanyifeng.com/blog/2023/02/weekly-issue-240.html) (#240)

[Tư duy sản phẩm hóa](https://www.ruanyifeng.com/blog/2021/12/weekly-issue-190.html) (#190)

(Hết)
