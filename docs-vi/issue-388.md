# Kiểm thử là "hào bảo vệ" mới

Đây là nơi ghi lại những nội dung công nghệ đáng chia sẻ hàng tuần, xuất bản vào mỗi thứ Sáu.

Tạp chí này là [nguồn mở](https://github.com/ruanyf/weekly), rất hoan nghênh các bạn [đóng góp nội dung](https://github.com/ruanyf/weekly/issues). Ngoài ra còn có dịch vụ ["Ai đang tuyển dụng"](https://github.com/ruanyf/weekly/issues/9088), nơi đăng tải thông tin tuyển dụng lập trình viên. Để hợp tác, vui lòng [liên hệ qua email](mailto:yifeng.ruan@gmail.com) (yifeng.ruan@gmail.com).

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030804.webp)

Tại một khu danh lam thắng cảnh ở Phù Lăng, Trùng Khánh, người ta đã dựng nên "Cầu treo cự thạch" đầu tiên trên thế giới. Mặt cầu được ghép từ những khối đá khổng lồ, chỉ cần sẩy chân một chút là có thể bước hụt xuống dưới. ([via](https://www.cbg.cn/a/77561/20260214/7b37135efeb74f0fbbaf272a9b7f6ae0.html))

## Kiểm thử là "hào bảo vệ" mới

[Next.js](https://nextjs.org) hiện là khung làm việc (framework) JS hàng đầu thế giới. Tôi ước tính có đến một nửa số ứng dụng JS full-stack mà chúng ta gặp hiện nay được phát triển bằng nó.

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022808.webp)

Nhưng cách đây hai tuần, một tin tức đã làm lung lay vị thế của framework này.

Một kỹ sư từ Cloudflare đã [tuyên bố](https://blog.cloudflare.com/vinext/) rằng **anh chỉ mất đúng một tuần để dùng AI tái hiện lại Next.js**, đặt tên là [vinext](https://vinext.io/).

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022809.webp)

Thực tế, anh chỉ mất một ngày để tạo ra bản mẫu đầu tiên, những ngày còn lại là để hoàn thiện.

> "Tôi bắt tay vào làm từ ngày 13/2. Ngay đêm hôm đó, các tính năng cơ bản đã xong. Chiều hôm sau, 10 trên 11 bộ định tuyến (router) đã hoàn thành. Đến ngày thứ ba, nó đã được triển khai lên máy chủ của chúng tôi và chạy mượt mà cơ chế hydrat hóa phía máy khách. Những ngày tiếp theo tôi tập trung vào bảo mật, xử lý các trường hợp biên và mở rộng bộ kiểm thử để đạt tỷ lệ bao phủ API lên tới 94%."

Điều đáng nói là bản tái hiện mới này còn có hiệu năng tốt hơn bản gốc.

> "Kết quả thử nghiệm sớm cho thấy tốc độ xây dựng (build) nhanh gấp 4 lần, dung lượng gói tin phía máy khách giảm 57%. Các ứng dụng Next.js thực tế đã có thể chạy trực tiếp trên nền tảng này."

Mã nguồn của vinext đã được [công khai trên GitHub](https://github.com/cloudflare/vinext).

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022810.webp)

Theo tôi, **đây là một đòn giáng cực mạnh vào Next.js**. Next.js là sản phẩm của công ty Vercel, với một đội ngũ lập trình viên hùng hậu, tiêu tốn hàng núi tiền và đã phát triển suốt 10 năm qua. Dù là nguồn mở, nhưng họ thu phí từ các dịch vụ đám mây, plugin và giao diện, với doanh thu năm ngoái đạt 200 triệu USD.

**Cái gọi là "hào bảo vệ" (moat) tưởng chừng bất khả xâm phạm đó đã sụp đổ trước AI**. Một kỹ sư đơn độc trong một tuần đã làm được việc của cả một đội ngũ trong mười năm. Các ứng dụng web hiện tại thậm chí chẳng cần sửa một dòng code nào, cứ thế bê sang là chạy.

Bạn có biết chi phí là bao nhiêu không? Tiền Token AI chỉ tốn vỏn vẹn 1.100 USD!

Vậy thì Vercel làm sao có thể tiếp tục rót tiền vào phát triển Next.js nữa, và khách hàng liệu còn muốn trả phí cao cho những tính năng mà AI có thể tái tạo trong nháy mắt? Mở rộng ra, mọi phần mềm thương mại đều đang bị đe dọa. "Hào bảo vệ" bằng mã nguồn không còn nữa.

Vậy các công ty phần mềm phải làm gì để bảo vệ mình? **Chìa khóa nằm ở các kịch bản kiểm thử (test cases)**.

Sở dĩ kỹ sư Cloudflare thành công là vì Next.js có tài liệu quá đầy đủ và hệ thống test case hoàn chỉnh. AI chỉ cần mô phỏng từng API sao cho vượt qua được các bài kiểm tra cũ là có thể đảm bảo tương thích 100%. Nếu không có test case, chẳng ai biết mã nguồn mới có hoạt động đúng như cũ hay không, và chẳng ai dám đưa nó vào sản xuất.

Trong tương lai, để tránh bị AI "copy-paste", các dự án phần mềm lớn chắc chắn sẽ bảo mật hệ thống kiểm thử của mình. **Kiểm thử chính là hào bảo vệ mới.**

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030601.webp)

SQLite – hệ quản trị cơ sở dữ liệu phổ biến nhất thế giới – là một ví dụ điển hình. Mã nguồn của nó chỉ có 156.000 dòng, nhưng các kịch bản kiểm thử lên tới [92,05 triệu dòng](https://sqlite.org/testing.html), gấp 590 lần! Trong đó, bộ test quan trọng nhất là TH3 vẫn được giữ kín. Chính những bài kiểm tra bí mật này đã khiến SQLite gần như không thể bị sao chép hoàn hảo.

Gần đây, một dự án nguồn mở khác là [tldraw](https://github.com/tldraw/tldraw/issues/8082) cũng đang rục rịch chuyển hệ thống test case sang dạng đóng.

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022811.webp)

Dù việc đóng kín test case có thể không tốt cho sự phát triển của nguồn mở, nhưng các nhà phát triển cần bảo vệ lợi ích của mình. Trước sự bành trướng của AI, đây có lẽ là lựa chọn tất yếu.

## Vấn đề bản quyền khi AI tái hiện phần mềm

Việc AI tái hiện lại phần mềm cũng đang gây ra nhiều [tranh cãi về pháp lý](https://tuananh.net/2026/03/05/relicensing-with-ai-assisted-rewrite/).

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030602.webp)

Next.js sử dụng giấy phép MIT cực kỳ cởi mở nên không sao. Nhưng với dự án [chardet](https://github.com/chardet/chardet), mọi chuyện lại khác. chardet vốn dùng giấy phép LGPL với nhiều hạn chế, nhưng sau khi được AI viết lại, nó đã bị đổi sang giấy phép MIT, khiến tác giả gốc phản ứng dữ dội.

Dư luận đang chia làm hai phe. Một bên cho rằng AI chỉ tái hiện chức năng và giao diện, còn mã nguồn hoàn toàn khác nên có thể đổi giấy phép. Bên kia lại lập luận theo quy định của GPL: mọi tác phẩm phái sinh đều không được đổi giấy phép, mà AI tái hiện chính là một dạng phái sinh.

Rắc rối hơn nữa là luật pháp Mỹ quy định sản phẩm do AI tạo ra không có bản quyền. Nghĩa là phần mềm do AI viết lại có thể rơi vào phạm vi công cộng, mọi giấy phép đi kèm đều vô hiệu. Nếu vậy, các loại giấy phép phần mềm từ nay về sau có lẽ chẳng còn mấy ý nghĩa.

## Tin công nghệ

1. [AI sửa lời lăng mạ](https://decrypt.co/360183/roblox-using-ai-rewrite-chat-swears-slurs-real-time)

Nền tảng trò chơi Roblox [thông báo](https://ir.roblox.com/news/news-details/2026/Roblox-Launches-Real-Time-Chat-Rephrasing-to-Maintain-Civility-and-Gameplay-Flow/default.aspx) sẽ dùng AI để chỉnh sửa trực tiếp các đoạn chat của người chơi sao cho lịch sự hơn.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030701.webp)

Trước đây, khi người chơi chửi thề, hệ thống sẽ lọc thành chuỗi `####`. Giờ đây, AI sẽ viết lại cả câu để ý tứ trở nên nhã nhặn hơn, khiến đối phương thậm chí không nhận ra mình đang bị mắng. Dù có vẻ hơi "giả trân", nhưng điều này thực sự cần thiết để giữ gìn môi trường giao tiếp lành mạnh.

2. [Internet bằng tia laser trên máy bay](https://www.esa.int/Applications/Connectivity_and_Secure_Communications/World-first_gigabit-per-second_laser_link_between_aircraft_and_geostationary_satellite)

Cơ quan Vũ trụ Châu Âu đã thử nghiệm thành công việc kết nối internet cho máy bay thông qua tia laser trỏ thẳng đến vệ tinh.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030704.webp)

Hiện nay internet trên máy bay chủ yếu dùng sóng vô tuyến (như Starlink). Ưu điểm của laser là băng thông cực lớn và không bị hạn chế bởi phổ tần vô tuyến.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030705.webp)

Tốc độ trong thử nghiệm đạt tới 2,6Gbps, nhanh gấp 8 - 10 lần so với Starlink. Tuy nhiên, nhược điểm là laser yêu cầu đường truyền thẳng tắp, không được có mây hay chướng ngại vật khí quyển, nên có lẽ chỉ dùng được khi máy bay đã lên độ cao ổn định.

3. [Ý kiến chuyên gia của Grammarly](https://www.theverge.com/ai-artificial-intelligence/890921/grammarly-ai-expert-reviews)

Grammarly có tính năng trả phí cho phép các chuyên gia nhận xét bài viết của bạn.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031002.webp)

Một người dùng đã vô cùng kinh ngạc khi thấy tên sếp cũ của mình trong danh sách chuyên gia, trong khi ông ấy đã qua đời.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031003.webp)

Hóa ra đó không phải người thật, mà là AI đã tạo ra các "phiên bản kỹ thuật số" của các chuyên gia dựa trên các bài viết cũ của họ để đưa ra nhận xét. Điều này dấy lên tranh cãi về quyền được tạo ra các bản sao AI của người khác mà không có sự cho phép.

4. [Thùng thư năng lượng mặt trời](https://www.bbc.com/news/articles/cgln72rgrero)

Royal Mail (Bưu điện Hoàng gia Anh) đang biến 3.500 thùng thư truyền thống thành các "thùng thư năng lượng mặt trời".

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110505.webp)

Phần mái của chúng được lắp các tấm pin quang điện, giúp chuyển đổi công năng từ nhận thư sang nhận và gửi các bưu kiện nhỏ.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110506.webp)

Cách làm này vừa giữ lại được hình ảnh biểu tượng của những thùng thư đỏ trên đường phố, vừa đáp ứng được nhu cầu thực tế của người dân.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110507.webp)

## Bài viết

1. [Tấn công tiêm nhiễm vào tiêu đề Issue trên GitHub](https://grith.ai/blog/clinejection-when-your-ai-tool-installs-another) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030703.webp)

Một vụ tấn công thực tế đầu tiên vào mô hình AI. Kẻ tấn công đã chèn mã độc vào tiêu đề Issue để lừa AI của dự án Cline, từ đó chiếm được quyền phát hành phiên bản độc hại lên npm.

2. [Đánh giá lại tệp AGENTS.md](https://www.infoq.com/news/2026/03/agents-context-file-value-review/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030901.webp)

Một nghiên cứu mới cho thấy tệp `AGENTS.md` đôi khi lại gây cản trở thay vì hỗ trợ AI lập trình. Nó khiến mô hình "suy nghĩ" nhiều hơn làm tăng chi phí nhưng kết quả lại không thực sự tốt hơn.

3. [Hành trình 9 năm của Temporal API](https://bloomberg.github.io/js-blog/post/temporal/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031205.webp)

Temporal API cuối cùng đã được đưa vào chuẩn ES2026. Đây là hồi ức của người soạn thảo tiêu chuẩn này về hành trình gian nan kéo dài gần một thập kỷ.

4. [Bài kiểm tra mức độ "nói nhảm" của AI](https://decrypt.co/360596/benchmark-test-measures-ai-bullshit-most-models-fail) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031206.webp)

[BuillshitBench](https://petergpt.github.io/bullshit-benchmark/viewer/index.v2.html) chuyên đưa ra những câu hỏi vô nghĩa để xem liệu AI có đủ thông minh để nhận ra hay vẫn trả lời một cách nghiêm túc.

5. [Chỉ cần CSS thuần là đủ](https://www.zolkos.com/2025/12/03/vanilla-css-is-all-you-need) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120704.webp)

Bài viết chứng minh rằng không cần các framework như Tailwind hay công cụ như Sass, chỉ với CSS thuần túy bạn vẫn có thể xây dựng nên những sản phẩm tuyệt vời.

6. [Vật lý học của việc... đi vệ sinh](https://theconversation.com/physics-of-poo-why-it-takes-you-and-an-elephant-the-same-amount-of-time-76696) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030802.webp)

Một bài viết khoa học vui giải thích tại sao mọi loài động vật từ chuột đến voi đều có thời gian đi vệ sinh trung bình khoảng 12 giây.

## Công cụ

1. [KULA](https://github.com/c0m4r/kula)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030706.webp)

Công cụ giám sát máy chủ Linux siêu nhẹ, chỉ gồm một tệp tin thực thi duy nhất.

2. [AnsiSaver](https://github.com/lardissone/ansi-saver)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030803.webp)

Trình bảo vệ màn hình (screensaver) cho máy Mac sử dụng các ký tự Ansi đầy màu sắc.

3. [upiano](https://github.com/eliasdorneles/upiano)

![](https://cdn.beekka.com/blogimg/asset/202308/bg2023081012.webp)

Chơi đàn piano ngay trên giao diện dòng lệnh.

4. [WSL Distro Manager](https://github.com/bostrot/wsl2-distro-manager)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031207.webp)

Ứng dụng nguồn mở giúp quản lý các bản phân phối WSL trên Windows qua giao diện đồ họa.

5. [Mole](https://github.com/tw93/Mole)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031213.webp)

Công cụ dọn dẹp và tối ưu hóa hệ thống cho máy Mac.

6. [PipeGate](https://github.com/janbjorge/pipegate)

Công cụ tạo đường hầm ánh xạ dịch vụ nội mạng ra ngoài internet bằng các đoạn mã Python đơn giản.

7. [HookListener](https://www.hooklistener.com)

![](https://cdn.beekka.com/blogimg/asset/202412/bg2024121804.webp)

Công cụ trực tuyến để quản lý và kiểm thử Webhook.

8. [Sentinel](https://github.com/suzuran0y/CCTV-Smartphone-AI-Monitoring)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031201.webp)

Biến điện thoại Android cũ thành camera giám sát tích hợp AI.

9. [Flux Monitor](https://github.com/chentao1006/FluxMonitor)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031203.webp)

Bảng điều khiển theo dõi hệ thống cho người dùng Mac.

## AI

1. [Agentic Metric](https://github.com/MrQianjinsi/agentic-metric)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030603.webp)

Công cụ dòng lệnh theo dõi mức độ sử dụng của các trợ lý lập trình như Claude Code, Codex.

2. [cc-connect](https://github.com/chenhg5/cc-connect)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031202.webp)

Kết nối các công cụ lập trình AI với các ứng dụng trò chuyện trên điện thoại.

3. [Page Agent](https://github.com/alibaba/page-agent)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030702.webp)

Chỉ cần nhúng thư viện JS này vào trang web, bạn có thể điều khiển trang web đó bằng ngôn ngữ tự nhiên.

4. [Agent Safehouse](https://github.com/eugene1g/agent-safehouse)

Công cụ sandbox cho macOS để chạy các trình lập trình AI một cách an toàn.

5. [Repo Tokens](https://github.com/qwibitai/nanoclaw/tree/main/repo-tokens)

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022801.webp)

GitHub Action giúp hiển thị số lượng Token của toàn bộ kho mã nguồn dưới dạng một chiếc nhãn (badge) trực quan.

## Tài nguyên

1. [World Monitor (Giám sát thế giới)](https://www.worldmonitor.app)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030801.webp)

Bảng tin thời gian thực về tình hình thế giới, tổng hợp từ nhiều nguồn tin khác nhau.

2. [Khám phá nhà máy lọc dầu](https://fuelingcuriosity.com/game.html)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031204.webp)

Trang web tương tác sinh động giải thích quy trình biến dầu thô thành xăng dầu.

3. [Mechanical Pencil](https://mechanical-pencil.com)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031001.webp)

Hoạt ảnh giải thích cơ chế hoạt động của các vật dụng nhỏ như bút chì bấm, bật lửa.

## Hình ảnh

1. [Phương pháp thay thế mật khẩu](https://tesseral.com/blog/i-designed-some-more-user-friendly-methods-for-multi-factor-authentication)

Một lập trình viên đã nảy ra ý tưởng dùng bộ bài Tây làm mật khẩu. Bạn chọn ra 5 quân bài theo thứ tự, và lần sau đăng nhập phải chọn đúng y hệt như vậy. Thú vị đấy chứ?

![](https://cdn.beekka.com/blogimg/asset/202507/bg2025073110.webp)

## Điểm tin

1. [Sự sụp đổ của xã hội phức tạp](https://news.ycombinator.com/item?id=31670526)

Lịch sử cho thấy khi độ phức tạp của một xã hội vượt quá ngưỡng chịu đựng, nó sẽ sụp đổ. Các đế chế như La Mã hay Maya đều từng đối mặt với kẻ thù mang tên "sự phức tạp": quá nhiều tầng lớp quan liêu, quá nhiều luật lệ khiến chi phí vận hành xã hội trở nên khổng lồ nhưng hiệu quả mang lại ngày càng thấp.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031214.webp)

## Phát ngôn

1.

Năm 2021, tôi cảm thấy thật tuyệt vời khi là một kỹ sư phần mềm. Nhưng đến năm 2026, tôi không còn chắc ngành này sẽ ra sao trong mười năm tới. Có lẽ công việc mà tôi yêu thích sắp sửa biến mất.

-- [《Tôi không biết liệu mười năm nữa công việc của mình còn tồn tại không》](https://www.seangoedecke.com/will-my-job-still-exist/)

2.

Đối đầu với một AI mạnh mẽ sẽ có cảm giác thế nào? Bạn sẽ thấy mình bỗng nhiên yếu đi một cách khó hiểu, vì mọi bước đi của AI đều vượt xa dự tính của bạn.

-- probablydance.com

3.

Đọc sách về kinh doanh là lãng phí thời gian. Chúng biến những câu chuyện đơn giản thành lời khuyên sáo rỗng và dùng những khẩu hiệu truyền cảm hứng để che lấp đi sự phức tạp của thị trường.

-- [《Đọc sách kinh doanh là lãng phí thời gian》](https://antemedian.substack.com/p/why-reading-business-books-is-a-waste)

4.

Tôi thường yêu cầu AI đọc tài liệu hướng dẫn của một công cụ mới bằng cách ra lệnh "chạy `xxx-tool --help`", và thế là nó học được cách dùng ngay lập tức.

-- Simon Willison.

5.

Thời gian là tài nguyên duy nhất không thể tái tạo. Các mô hình AI lớn là cách rẻ nhất mà tôi biết để mua thêm thời gian cho chính mình.

-- [《Đừng quá lăn tăn về phí thuê bao AI》](https://steipete.me/posts/2025/stop-overthinking-ai-subscriptions)

## Nhìn lại các năm trước

[Lập trình low-code có lẽ khó thành công](https://www.ruanyifeng.com/blog/2025/03/weekly-issue-341.html) (#341)

[AI không có hào bảo vệ](http://www.ruanyifeng.com/blog/2024/03/weekly-issue-291.html) (#291)

[Động lực tăng trưởng của Trung Quốc nằm ở vùng nội địa](http://www.ruanyifeng.com/blog/2023/02/weekly-issue-241.html) (#241)

[Con đường tự do tài chính của một lập trình viên](http://www.ruanyifeng.com/blog/2022/01/weekly-issue-191.html) (#191)

(Hết)
