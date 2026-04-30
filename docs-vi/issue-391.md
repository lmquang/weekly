# Sự phân hóa giàu nghèo trong thời đại AI

Bản tin này ghi lại những nội dung công nghệ đáng chia sẻ hàng tuần, phát hành vào thứ Sáu.

Tạp chí này [mã nguồn mở](https://github.com/ruanyf/weekly), hoan nghênh bạn [đóng góp](https://github.com/ruanyf/weekly/issues). Ngoài ra còn có dịch vụ ["Ai đang tuyển dụng"](https://github.com/ruanyf/weekly/issues/9454) dành cho các lập trình viên. Nếu muốn hợp tác, bạn hãy [liên hệ qua email](mailto:yifeng.ruan@gmail.com) (yifeng.ruan@gmail.com) nhé.

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040107.webp)

Một góc trang trí tường tại một nhà hàng ở Thượng Hải. (via [monana3838@Threads](https://www.threads.com/@monana3838/post/DWjVcmcAoh4))

## Sự phân hóa giàu nghèo trong thời đại AI

Tôi càng ngày càng cảm thấy AI khác biệt hoàn toàn với những công nghệ trước đây. Nó không chỉ mang lại sự thay đổi về kỹ thuật, mà còn kéo theo những biến động sâu sắc về mặt xã hội.

Nói một cách đơn giản: AI sẽ làm gia tăng sự phân hóa giàu nghèo.

Thông thường, công nghệ sinh ra để xóa nhòa khoảng cách, tạo ra cái gọi là "sự bình đẳng trong tiêu thụ". Tức là dù giàu hay nghèo, chúng ta đều dùng chung một loại sản phẩm.

Ví dụ, tất cả chúng ta đều uống chung một loại Coca-Cola, dùng chung chiếc iPhone hay lái chung một chiếc Tesla. Thậm chí với Internet cũng vậy, tỷ phú Elon Musk cũng dùng chung một website, một ứng dụng di động giống hệt như bạn.

Thế nhưng, các mô hình AI thì không như thế. **Trước đại diện của trí tuệ nhân tạo, sự bình đẳng này sẽ biến mất.**

Trong tương lai, người bình thường chắc chắn không đủ khả năng chi trả cho những mô hình AI hàng đầu. Thực tế điều này đã bắt đầu rồi. Gói lập trình AI đắt nhất hiện nay là Claude Code Max với mức phí 200 USD mỗi tháng, một con số mà nhiều người đã phải lắc đầu.

OpenAI từng có ý định tung ra [gói dịch vụ lên tới 20.000 USD/tháng](https://www.thepaper.cn/newsDetail_forward_30320495) để cung cấp những mô hình đỉnh cao với khả năng xử lý không giới hạn.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032207.webp)

Nếu gói cước này thực sự ra mắt, rõ ràng nó chỉ dành cho giới siêu giàu.

Điều này phản ánh một sự thật phũ phàng: **Tiền nào của nấy, mô hình càng đắt thì hiệu quả càng cao**. Bởi vì sức mạnh của AI tỷ lệ thuận với năng lực tính toán. Muốn có nhiều tính toán hơn, cửa sổ ngữ cảnh lớn hơn, tham số nhiều hơn, bạn buộc phải chi rất nhiều tiền.

Điều này đi ngược lại với logic của hàng công nghiệp thông thường. Hàng hóa công nghiệp có hiệu ứng quy mô: sản lượng càng cao, chi phí đơn vị càng giảm. Khi sản xuất đại trà, giá thành sẽ ngày càng rẻ.

Nhưng **mô hình AI không có hiệu ứng quy mô kiểu đó**. Việc sản xuất mô hình ở quy mô lớn đòi hỏi thêm rất nhiều máy chủ. Điều này không làm giảm chi phí đơn vị, thậm chí còn khiến nó đắt đỏ hơn do phải mở rộng hạ tầng, cải tạo hệ thống điện nước cho các trung tâm dữ liệu khổng lồ.

Xã hội tương lai có lẽ sẽ phân cực: người giàu và người nghèo dùng những mô hình khác nhau. Những dịch vụ cao cấp nhất như lập kế hoạch, tư vấn, sáng tạo nội dung, tự động hóa... sẽ yêu cầu mức phí sử dụng trên trời. Trong khi đó, người bình thường sẽ chấp nhận dùng các mô hình miễn phí với hiệu quả ở mức trung bình.

Tuy nhiên, Elon Musk [vừa mới nhận định](https://wap.cj.sina.cn/7x24/4762771) rằng tương lai vẫn còn một khả năng khác.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032206.webp)

Ông cho rằng năng lực tính toán thực chất là một dạng chuyển hóa của năng lượng. Nếu loài người có thể tạo ra nguồn năng lượng dồi dào và rẻ tiền (như năng lượng mặt trời ngoài không gian chẳng hạn), thì tính toán sẽ trở nên rẻ đến mức ai cũng có thể tiếp cận những mô hình tốt nhất.

Liệu kịch bản này có khả thi không? Tôi không chắc, nhưng cảm thấy viễn cảnh đầu tiên có vẻ thực tế hơn nhiều.

## Một thước đo mới cho năng lực mô hình

Làm sao để đánh giá sức mạnh của một mô hình AI?

Cách làm phổ biến hiện nay là dùng một bộ đề thi (benchmark) để tính điểm. Nhược điểm của nó là chỉ dùng để so sánh hàng ngang, chứ rất khó để đo lường tốc độ tiến bộ theo thời gian.

Gần đây, một bài báo khoa học đã đề xuất [một cách tiếp cận mới](https://emptysqua.re/blog/review-measuring-ai-ability-to-complete-long-software-tasks/). Các nhà khoa học bắt đầu bằng việc tính toán xem con người mất bao lâu để hoàn thành một nhiệm vụ cụ thể. Ví dụ, tính 4 + 5 + 7 mất 2 giây, nhưng tính 37 * 52 * 19 có thể mất tới 1 phút.

Sau đó, họ kiểm tra xem liệu mô hình AI có thể hoàn thành nhiệm vụ đó với tỷ lệ thành công 50% hay không.

Kết quả nghiên cứu cho thấy: GPT-2 có thể hoàn thành những việc con người làm trong 2 giây; Claude 3.7 Sonnet vọt lên mức 50 phút; O3 tiệm cận 2 giờ; và Opus 4.6 lên tới khoảng 12 giờ. Nghĩa là những công việc mà một chuyên gia con người phải mất 12 tiếng mới xong thì Opus 4.6 có xác suất giải quyết được là 50%.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040201.webp)

Nhìn vào biểu đồ trên, bạn sẽ thấy tốc độ tiến hóa của AI là một đường thẳng trên thang đo logarit.

**Cứ sau mỗi 7 tháng, độ khó của nhiệm vụ mà AI có thể giải quyết được (với xác suất 50%) lại tăng gấp đôi**. Theo đà này, trong khoảng năm 2027 đến 2031, AI sẽ có thể đảm đương những công việc mà một chuyên gia con người phải mất cả tháng trời mới hoàn thành.

Nếu nghiên cứu này đúng, nó đồng nghĩa với việc các mô hình ra mắt vào cuối năm sẽ mạnh gấp đôi so với những mô hình hồi đầu năm.

## Tin công nghệ

1. [Quà tặng ẩn trong điều khoản sử dụng](https://www.cape.co/blog/easter-egg-in-privacy-policy)

Các bản "Điều khoản sử dụng" thường dài dằng dặc và khô khan đến mức chẳng ai buồn đọc. Một nhà mạng ở Mỹ muốn kiểm chứng xem khách hàng có thực sự quan tâm đến quyền lợi của mình không, nên đã giấu một "quả trứng phục sinh" (easter egg) vào giữa bản hợp đồng.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026033101.webp)

Dòng chữ đó viết: "Nếu bạn đọc được dòng này, hãy gửi email cho chúng tôi để nhận một chuyến du lịch Thụy Sĩ miễn phí." Hai tuần sau mới có người đầu tiên gửi mail hỏi xem đây có phải là thật không. Và thế là cô ấy có một chuyến đi Thụy Sĩ miễn phí vì là người duy nhất thực sự đọc kỹ bản hợp đồng.

Rõ ràng, dù có tặng quà thì cũng chẳng ai muốn đọc những thứ đó. Kinh nghiệm của tôi là hãy ném nó cho AI và hỏi: "Bản hợp đồng này có điều khoản nào bất lợi cho tôi không?", bạn sẽ có câu trả lời ngay lập tức.

2. [Sơn móng tay cho màn hình cảm ứng](https://www.livescience.com/chemistry/chemistry-student-develops-clear-polish-that-turns-your-fingernail-into-a-touch-screen-stylus)

Màn hình cảm ứng điện dung hiện nay có một nhược điểm là không dùng được khi đeo găng tay. Lý do là găng tay không dẫn điện, khiến màn hình không nhận diện được sự thay đổi điện trường.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032802.webp)

Một sinh viên ngành hóa tại Mỹ đã nảy ra ý tưởng cực kỳ đơn giản: tạo ra một loại sơn móng tay trong suốt có chứa các mẩu kim loại siêu nhỏ giúp dẫn điện. Bạn có thể sơn lên đầu ngón tay của găng tay để sử dụng điện thoại mà không cần tháo găng, hoặc sơn trực tiếp lên móng tay như một lớp sơn bóng thông thường.

3. [Quảng cáo trong Pull Request của Copilot](https://www.theregister.com/2026/03/30/github_copilot_ads_pull_requests/)

Copilot, trợ lý AI của GitHub, vừa bị người dùng phát hiện là tự ý chèn quảng cáo vào mã nguồn.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040106.webp)

Trong một PR do Copilot tự động gửi lên, nó đã lén chèn một đoạn quảng cáo cho ứng dụng Raycast ở cuối phần mô tả. Khi tìm kiếm trên GitHub, người ta phát hiện có tới hơn 11.400 PR chứa cùng một đoạn quảng cáo này. GitHub đã phải tạm dừng tính năng này sau khi bị phản ứng dữ dội. Đây là một dấu hiệu cho thấy các ông lớn đang tìm mọi cách để tận dụng người dùng nhằm tăng doanh thu.

## Bài viết hay

1. [Review Xiaomi MiMo v2 Pro](https://decrypt.co/362633/xiaomi-mimo-v2-pro-review-so-good-mistaken-deepseek-v4) (Tiếng Anh)

Dòng mô hình lớn MiMo V2 mới của Xiaomi đang nhận được những đánh giá rất cao từ giới chuyên môn quốc tế về hiệu năng thực tế.

2. [Tôi dùng AI để viết một engine JavaScript](https://p.ocmatos.com/blog/jsse-a-javascript-engine-built-by-an-agent.html) (Tiếng Anh)

Chỉ trong 6 tuần, tác giả đã dùng AI để xây dựng một engine JavaScript vượt qua 100% các bài test của bộ test262 tiêu chuẩn. Một minh chứng cho sức mạnh khủng khiếp của lập trình bằng AI.

3. [Bên trong thư mục .claude/](https://blog.dailydoseofds.com/p/anatomy-of-the-claude-folder) (Tiếng Anh)

Khám phá xem Claude Code thực sự lưu trữ những gì bên dưới thư mục ẩn .claude mỗi khi bạn chạy các tác vụ lập trình.

4. [Nhập môn Consistent Hashing](https://eli.thegreenplace.net/2025/consistent-hashing) (Tiếng Anh)

Một thuật toán quan trọng trong việc quản lý bộ nhớ đệm giúp hệ thống vận hành ổn định ngay cả khi tăng hoặc giảm số lượng máy chủ.

5. [Biến laptop thành màn hình cho máy tính đơn bo](https://danielmangum.com/posts/laptop-hdmi-monitor-sbc/) (Tiếng Anh)

Mẹo nhỏ sử dụng card ghi hình (capture card) để dùng laptop làm màn hình hiển thị cho các thiết bị như Raspberry Pi.

## Công cụ

1. [EmDash](https://github.com/emdash-cms/emdash)

Một bản clone của WordPress được viết bằng TypeScript và hỗ trợ AI, hứa hẹn mang lại những trải nghiệm quản trị nội dung mới mẻ.

2. [SubsTracker](https://github.com/wangwangit/SubsTracker)

Hệ thống quản lý các dịch vụ trả phí (subscription) chạy trên Cloudflare Workers, giúp nhắc lịch hết hạn qua Telegram hoặc Webhook. ([@wangwangit](https://github.com/ruanyf/weekly/issues/9411) đóng góp)

3. [OpeniLink Hub](https://github.com/openilink/openilink-hub)

Nền tảng quản lý robot WeChat mã nguồn mở, cho phép cài đặt thêm các ứng dụng để mở rộng tính năng cho bot. ([@xixihhhh](https://github.com/ruanyf/weekly/issues/9404) đóng góp)

4. [Lixian.Online](https://lixian.online/)

Công cụ giúp tải các gói cài đặt offline cho VSCode, Chrome Extension hay Docker. ([@LiaoGuoYin](https://github.com/ruanyf/weekly/issues/9455) đóng góp)

5. [Rename.Tools](https://rename.tools/zh/app)

Công cụ đổi tên file hàng loạt trực tiếp trên trình duyệt với nhiều quy tắc tùy biến linh hoạt. ([@chenz24](https://github.com/ruanyf/weekly/issues/9461) đóng góp)

6. [FontInAss](https://github.com/Yuri-NagaSaki/FontInAss)

Giúp nhúng trực tiếp các font chữ cần thiết vào file phụ đề, đảm bảo hiển thị đúng trên mọi thiết bị. ([@Yuri-NagaSaki](https://github.com/ruanyf/weekly/issues/9466) đóng góp)

7. [pretext.video](https://github.com/fifteen42/pretext-video)

Một ứng dụng thú vị giúp hiển thị hình ảnh từ camera dưới dạng các ký tự văn bản được sắp xếp theo thời gian thực. ([@fifteen42](https://github.com/ruanyf/weekly/issues/9472) đóng góp)

8. [OxideTerm](https://github.com/AnalyseDeCircuit/oxideterm)

Phần mềm SSH terminal đa nền tảng viết bằng Rust, sử dụng framework Tauri cho hiệu năng mượt mà. ([@AnalyseDeCircuit](https://github.com/ruanyf/weekly/issues/9474) đóng góp)

9. [wtree](https://github.com/FatDoge/wtree)

Giao diện đồ họa giúp bạn quản lý các git worktree một cách trực quan và dễ dàng hơn. ([@FatDoge](https://github.com/ruanyf/weekly/issues/9483) đóng góp)

## AI liên quan

1. [Open Agent SDK](https://github.com/shipany-ai/open-agent-sdk)

Giải pháp thay thế mã nguồn mở cho SDK của Claude Code, giúp bạn phát triển các AI Agent mà không cần phụ thuộc vào tiến trình CLI cục bộ. ([@idoubi](https://github.com/ruanyf/weekly/issues/9473) đóng góp)

2. [Antigravity Gateway](https://github.com/Truthan49/Antigravity-Everywhere)

Bảng điều khiển tập trung giúp quản lý mọi AI Agent trên máy bạn với các tính năng phân vùng làm việc và cộng tác từ xa. ([@Mr-ZhangBo](https://github.com/ruanyf/weekly/issues/9395) đóng góp)

3. [ArcReel](https://github.com/ArcReel/ArcReel)

Chỉ cần nhập một cuốn tiểu thuyết, công cụ này sẽ tự động lên kịch bản, thiết kế nhân vật và tạo ra các đoạn video minh họa. ([@Pollo3470](https://github.com/ruanyf/weekly/issues/9393) đóng góp)

4. [TermCanvas](https://github.com/blueberrycongee/termcanvas)

Biến các terminal thành những mảnh ghép trên một mặt phẳng vô hạn, giúp việc quản lý các công cụ lập trình AI trở nên trực quan hơn. ([@blueberrycongee](https://github.com/ruanyf/weekly/issues/9434) đóng góp)

## Tài nguyên

1. [Hướng dẫn sử dụng Claude Code](https://claude.nagdy.me/)

Chuỗi bài tập tương tác giúp bạn nhanh chóng làm chủ công cụ lập trình AI mạnh mẽ này.

2. [Claude Code Unpacked](https://ccunpacked.dev/)

Giải mã cách thức hoạt động bên trong của Claude Code thông qua những sơ đồ minh họa sinh động.

3. [Machine Learning cho kỹ sư](https://github.com/dreddnafious/thereisnospoon/blob/main/ml-primer.md)

Tài liệu ngắn gọn giúp các kỹ sư phần mềm nhanh chóng nắm bắt các khái niệm cơ bản về học máy.

## Hình ảnh

1. [Cây của năm tại Châu Âu](https://nicenews.com/environment/european-tree-of-the-year-winners-2026/)

Mỗi năm Châu Âu đều tổ chức cuộc bình chọn "Cây của năm". Hoạt động này không chỉ nhằm vinh danh vẻ đẹp tự nhiên mà còn giúp nâng cao ý thức bảo vệ môi trường và thúc đẩy du lịch sinh thái cho các địa phương. Năm nay, danh hiệu cao quý thuộc về một cây sồi 400 tuổi tại Lithuania.

## Văn trích

1. [Càng dùng AI, tôi càng bớt lo lắng](https://simonwillison.net/2025/Jul/4/identify-solve-verify/)

Dù AI có lập trình giỏi đến đâu, tôi cũng không còn lo bị mất việc. Bởi vì viết code chỉ là một phần nhỏ trong quy trình. Công việc thực sự của chúng ta là **tìm ra vấn đề cần giải quyết, đưa ra giải pháp và xác thực xem nó có thực sự hiệu quả hay không**. AI có thể giúp chúng ta viết code nhanh hơn, nhưng nó vẫn cần con người định hướng và chốt kết quả. Đó mới là 80% giá trị của một lập trình viên.

2. [Sự bế tắc của Định luật Moore](https://bzolang.blog/p/the-unsustainability-of-moores-law)

Trong khi số lượng bóng bán dẫn tăng gấp đôi sau mỗi 2 năm, thì chi phí xây dựng nhà máy chip cũng tăng gấp đôi sau mỗi 5 năm. Hiện nay chỉ còn vài ông lớn đủ sức chạy đua trong cuộc chơi tốn kém hàng chục tỷ USD này. Sắp tới, Định luật Moore có lẽ sẽ lùi bước, nhường chỗ cho cuộc đua về sức mạnh tính toán tổng thể thay vì chỉ tập trung vào khả năng của một con chip đơn lẻ.

## Trích dẫn

1.

Việc để lộ file source map lên npm nghe có vẻ ngớ ngẩn, nhưng nếu bạn biết rằng phần lớn code đó do AI viết thì mọi chuyện lại trở nên rất dễ hiểu.

-- Một bình luận về sự cố lộ mã nguồn Claude Code

2.

Sự bùng nổ của AI sẽ khiến nhu cầu về các công việc văn phòng giảm đi, nhưng lại tạo ra rất nhiều cơ hội cho các thợ điện, thợ hàn hay thợ sửa ống nước.

-- Larry Fink, CEO BlackRock

3.

Việc để AI viết thay bạn cũng giống như việc bạn trả tiền để thuê người khác đi tập gym hộ mình vậy.

-- Đừng để AI viết thay bạn

4.

Công việc của lập trình viên không phải là gõ code, mà là quản lý sự phức tạp của phần mềm thông qua các trừu tượng hóa. Nếu bạn làm tốt việc đó, việc viết code sẽ trở nên vô cùng đơn giản.

-- Công việc của bạn không phải là lập trình

## Nhìn lại năm xưa

[Sản xuất đang dần chuyển dịch sang mô hình "kinh tế cộng tác"](https://www.ruanyifeng.com/blog/2025/04/weekly-issue-344.html) (#344)

[Những suy ngẫm từ trận hải chiến Nhai Môn](https://www.ruanyifeng.com/blog/2024/03/weekly-issue-294.html) (#294)

[Big Data đã đến hồi kết](https://www.ruanyifeng.com/blog/2023/03/weekly-issue-244.html) (#244)

[Người bi quan thường đúng, kẻ lạc quan mới thành công](https://www.ruanyifeng.com/blog/2022/02/weekly-issue-194.html) (#194)

(Hết)
