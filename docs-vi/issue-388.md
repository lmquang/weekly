---
tags: [Software, Phềm mềm, Testing, Kiểm thử, QA, Quản lý chất lượng, Security, Bảo mật, Programming, Lập trình]
---

# Kiểm thử chính là hào nước mới

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030804.webp)

Tại một khu thắng cảnh ở Phù Lăng, Trùng Khánh, người ta vừa khánh thành chiếc "cầu treo cự thạch" đầu tiên trên thế giới. Mặt cầu được ghép từ những tảng đá khổng lồ, chỉ cần một phút lơ là bạn có thể bước hụt bất cứ lúc nào. ([via](https://www.cbg.cn/a/77561/20260214/7b37135efeb74f0fbbaf272a9b7f6ae0.html))

## Kiểm thử chính là hào nước mới

[Next.js](https://nextjs.org) hiện đang là framework JS số một. Tôi đồ rằng phải đến một nửa số ứng dụng JS full-stack hiện nay được xây dựng dựa trên nó.

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022808.webp)

Thế nhưng, chỉ cách đây hai tuần, một tin tức chấn động đã làm lung lay vị thế của gã khổng lồ này.

Một kỹ sư tại Cloudflare vừa [tuyên bố](https://blog.cloudflare.com/vinext/) rằng anh ta đã **tái hiện thành công toàn bộ Next.js chỉ trong đúng một tuần bằng AI**, và đặt tên cho nó là [vinext](https://vinext.io/).

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022809.webp)

Thực tế, bản mẫu sản phẩm đã ra đời ngay trong ngày đầu tiên, những ngày sau đó chỉ là để tinh chỉnh thêm.

> "Tôi thực sự bắt tay vào làm từ ngày 13 tháng 2. Ngay tối hôm đó, các tính năng cơ bản đã xong xuôi. Chiều hôm sau, 10 trên tổng số 11 bộ định tuyến (router) đã sẵn sàng. Đến ngày thứ ba, nó đã được deploy lên server của chúng tôi với khả năng hydrate hoàn chỉnh ở phía client.
>
> Những ngày kế tiếp, tôi tập trung gia cố bảo mật: xử lý các trường hợp biên, mở rộng bộ kiểm thử, đưa tỷ lệ bao phủ API lên tới 94%."

Đáng kinh ngạc hơn, bản tái hiện này còn có hiệu năng vượt trội so với bản gốc.

> "Các bài kiểm tra benchmark sớm cho thấy tốc độ build nhanh gấp 4 lần, dung lượng gói bundle cho client giảm tới 57%. Thậm chí, một số ứng dụng Next.js thực tế đã có thể chạy trực tiếp trên nền tảng mới này."

Hiện mã nguồn của vinext đã được [công khai](https://github.com/cloudflare/vinext).

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022810.webp)

Tôi cho rằng đây là một cú giáng cực mạnh vào Next.js.

Next.js là sản phẩm của Vercel với đội ngũ phát triển hùng hậu và nguồn vốn đầu tư khổng lồ suốt 10 năm qua. Dù là mã nguồn mở, nhưng họ thu lợi từ bản Enterprise, các dịch vụ đám mây, plugin và giao diện, mang về doanh thu tới 200 triệu USD vào năm ngoái.

**Cái gọi là "hào nước" tưởng chừng bất khả xâm phạm đó giờ đây bỗng trở nên mỏng manh trước AI**. Một kỹ sư đơn độc chỉ mất một tuần để sao chép thành quả của cả một tập đoàn trong một thập kỷ. Các ứng dụng hiện tại thậm chí chẳng cần sửa một dòng code nào vẫn có thể chạy ngon lành trên bản tái hiện.

Bạn có biết chi phí cho việc này là bao nhiêu không? Chỉ vỏn vẹn 1.100 USD tiền Token AI!

Điều này khiến Vercel lâm vào thế khó: làm sao để tiếp tục đổ tiền vào phát triển Next.js khi khách hàng giờ đây chẳng còn mặn mà trả phí cao cho những tính năng có thể dễ dàng bị sao chép.

Nhìn rộng ra, mọi phần mềm thương mại đều đang đứng trước nguy cơ bị đe dọa. **Hào nước bằng mã nguồn đã không còn tồn tại. Chỉ với một khoản đầu tư nhỏ, AI có thể tái hiện bất kỳ phần mềm phức tạp nào.**

Vậy để tự bảo vệ mình, các công ty phần mềm sẽ làm gì? **Câu trả lời nằm ở các bộ kiểm thử (test cases).**

Lý do chính giúp kỹ sư Cloudflare tái hiện thành công Next.js là vì dự án này có tài liệu quá tốt, cộng đồng bài viết khổng lồ và bộ test cases cực kỳ đầy đủ. AI chỉ cần mô phỏng từng API và chạy thử với bộ test gốc, nếu vượt qua thì coi như đã tương thích 100%.

Nếu không có bộ test cases đó, chẳng ai dám chắc code AI viết ra có chạy đúng như bản gốc hay không, và đương nhiên không ai dám đưa nó vào môi trường thực tế.

Chúng ta có thể dự đoán rằng sắp tới, các dự án phần mềm lớn sẽ bảo mật bộ test cases của mình như một tài sản vô giá. **Kiểm thử mới chính là hào nước thực sự.**

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030601.webp)

Hãy nhìn vào [SQLite](https://sqlite.org), cơ sở dữ liệu phổ biến nhất thế giới. Mã nguồn của nó chỉ có 156.000 dòng, nhưng bộ test cases lên tới [92,05 triệu dòng](https://sqlite.org/testing.html) — gấp 590 lần!

Trong đó, bộ kiểm thử cốt lõi [TH3](https://sqlite.org/th3.html) hoàn toàn đóng nguồn. Nó dùng để kiểm tra các tình huống cực đoan trong ngành hàng không, y tế... vốn là những tài sản kỹ thuật cốt lõi. Chính những bộ test bảo mật này đã khiến SQLite gần như không thể bị sao chép hoàn hảo.

Gần đây, dự án mã nguồn mở [tldraw](https://github.com/tldraw/tldraw/issues/8082) cũng đã có động thái tương tự khi chuẩn bị đóng mã nguồn các bộ kiểm thử.

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022811.webp)

Thú thực, việc bảo mật test cases không có lợi cho sự phát triển chung của cộng đồng mã nguồn mở, nhưng các nhà phát triển buộc phải làm vậy để bảo vệ thành quả của mình trước sức mạnh ngày càng đáng sợ của AI.

## Vấn đề bản quyền khi AI tái hiện phần mềm

Việc AI tái hiện phần mềm cũng đang gây ra [nhiều tranh cãi](https://tuananh.net/2026/03/05/relicensing-with-ai-assisted-rewrite/) về mặt pháp lý.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030602.webp)

Next.js sử dụng giấy phép MIT rất thông thoáng nên việc tái hiện không gặp vấn đề bản quyền. Tuy nhiên, một dự án khác mang tên [chardet](https://github.com/chardet/chardet) bị tái hiện và đổi từ giấy phép LGPL sang MIT đã khiến tác giả gốc vô cùng phẫn nộ.

Cộng đồng mạng hiện đang chia làm hai phe:

Phe ủng hộ cho rằng AI chỉ tái hiện chức năng và giao diện API, còn mã nguồn bên trong hoàn toàn khác biệt, nên việc đổi giấy phép là hợp lệ.

Phe phản đối lập luận rằng theo quy định của GPL, mọi sản phẩm phái sinh đều không được phép đổi giấy phép, và bản tái hiện AI rõ ràng là một sản phẩm phái sinh.

Mọi chuyện còn rắc rối hơn khi luật pháp Mỹ hiện quy định các sản phẩm do AI tạo ra không có bản quyền và thuộc về cộng đồng. Điều này đồng nghĩa với việc **các phần mềm do AI tái hiện sẽ không thể áp dụng bất kỳ giấy phép nào, vì chúng vốn dĩ không có bản quyền ngay từ đầu.**

Nếu tiền lệ này được thiết lập, các loại giấy phép phần mềm sẽ trở nên vô nghĩa. Bất kể bạn dùng giấy phép gì, người khác chỉ cần dùng AI tái hiện lại là có thể lách luật một cách hợp pháp.

## Tin công nghệ

1、[AI chỉnh sửa lời thô tục](https://decrypt.co/360183/roblox-using-ai-rewrite-chat-swears-slurs-real-time)

Nền tảng game Roblox [thông báo](https://ir.roblox.com/news/news-details/2026/Roblox-Launches-Real-Time-Chat-Rephrasing-to-Maintain-Civility-and-Gameplay-Flow/default.aspx) sẽ dùng AI để chỉnh sửa trực tiếp các cuộc đối thoại của game thủ nhằm hướng tới một môi trường văn minh hơn.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030701.webp)

Trước đây, nếu bạn văng tục trong game, hệ thống sẽ che đi bằng ký hiệu `####`. Bây giờ, AI sẽ viết lại cả câu sao cho lịch sự mà vẫn giữ được ý nghĩa, khiến bạn không nhận ra đối phương đang định mắng mình. Dù nghe có vẻ hơi giả tạo, nhưng đây là một nỗ lực cần thiết để bảo vệ bầu không khí giao tiếp trên mạng.

2、[Internet bằng laser trên máy bay](https://www.esa.int/Applications/Connectivity_and_Secure_Communications/World-first_gigabit-per-second_laser_link_between_aircraft_and_geostationary_satellite)

Cơ quan Vũ trụ Châu Âu đã thử nghiệm thành công việc kết nối internet cho máy bay thông qua laser, cho phép truyền dữ liệu tốc độ cao giữa máy bay và vệ tinh.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030704.webp)

Hiện nay internet trên máy bay chủ yếu dùng sóng vô tuyến (như Starlink). Thử nghiệm này sử dụng laser với băng thông lớn hơn nhiều, đạt tốc độ 2,6Gbps, nhanh gấp 8-10 lần so với hiện tại.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030705.webp)

Hình trên là thiết bị đầu cuối laser được lắp trên cửa sổ máy bay. Nhược điểm là laser đòi hỏi đường truyền thẳng tắp, không bị mây che khuất, nên có lẽ chỉ dùng được khi máy bay đã lên tới độ cao lớn.

3、[Ý kiến chuyên gia của Grammarly](https://www.theverge.com/ai-artificial-intelligence/890921/grammarly-ai-expert-reviews)

Grammarly cung cấp tính năng "Ý kiến chuyên gia" (Expert reviews) để nhận xét bài viết của bạn.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031002.webp)

Một người dùng nước ngoài đã vô cùng sốc khi thấy sếp cũ của mình trong danh sách chuyên gia, trong khi ông ấy đã qua đời.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031003.webp)

Hóa ra đây không phải người thật, mà là AI tạo ra "phân thân kỹ thuật số" dựa trên các bài viết của họ để đưa ra nhận xét. Điều này gây tranh cãi về quyền tạo ra các bản sao AI dựa trên tên tuổi của người thật.

4、[Hòm thư năng lượng mặt trời](https://www.bbc.com/news/articles/cgln72rgrero)

Bưu điện Hoàng gia Anh đã biến 3.500 hòm thư truyền thống thành "hòm thư năng lượng mặt trời".

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110505.webp)

Phần mái được lắp tấm pin quang điện, và chức năng chuyển từ nhận thư sang nhận gửi các bưu kiện nhỏ.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110506.webp)

Cách làm này vừa bảo tồn được nét văn hóa của những hòm thư đỏ, vừa đáp ứng nhu cầu thực tế của thời đại.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110507.webp)

## Bài viết hay

1、[Tấn công Injection qua tiêu đề Issue trên GitHub](https://grith.ai/blog/clinejection-when-your-ai-tool-installs-another) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030703.webp)

Đây có thể là vụ tấn công "Prompt Injection" thực tế đầu tiên vào mô hình AI. Hacker chèn mã độc vào tiêu đề Issue để lừa công cụ AI lấy token npm và phát hành phiên bản phần mềm độc hại.

2、[Đánh giá lại AGENTS.md](https://www.infoq.com/news/2026/03/agents-context-file-value-review/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030901.webp)

Nghiên cứu mới chỉ ra rằng file AGENTS.md đôi khi lại gây tác dụng ngược khi khiến mô hình AI phải "suy nghĩ" quá nhiều, làm tăng chi phí nhưng lại không cải thiện được chất lượng mã nguồn.

3、[Hành trình 9 năm của Temporal API](https://bloomberg.github.io/js-blog/post/temporal/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031205.webp)

Temporal API cuối cùng đã chính thức trở thành một phần của tiêu chuẩn ES2026. Bài viết nhìn lại chặng đường gian nan để đưa một cú pháp mới vào JavaScript.

4、[Bài test khả năng "nói phét" của AI](https://decrypt.co/360596/benchmark-test-measures-ai-bullshit-most-models-fail) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031206.webp)

BullshitBench là một bộ câu hỏi đặc biệt để kiểm tra xem liệu AI có đủ thông minh để nhận ra những câu hỏi vô nghĩa, hay vẫn cố gắng trả lời một cách cực kỳ nghiêm túc.

5、[CSS thuần là đủ rồi](https://www.zolkos.com/2025/12/03/vanilla-css-is-all-you-need) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120704.webp)

37Signals chứng minh rằng bạn hoàn toàn có thể xây dựng những hệ thống lớn mà không cần đến framework hay công cụ xây dựng nào, chỉ với sức mạnh của CSS nguyên bản.

6、[Vật lý học về việc đi ngoài](https://theconversation.com/physics-of-poo-why-it-takes-you-and-an-elephant-the-same-amount-of-time-76696) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030802.webp)

Một bài viết khoa học giải thích tại sao hầu hết các loài động vật có vú đều có thời gian đi vệ sinh trung bình khoảng 12 giây, bất kể kích thước cơ thể lớn hay nhỏ.

## Công cụ

1、[KULA](https://github.com/c0m4r/kula)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030706.webp)

Công cụ giám sát server Linux siêu nhẹ chỉ với một file thực thi duy nhất.

2、[AnsiSaver](https://github.com/lardissone/ansi-saver)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030803.webp)

Trình bảo vệ màn hình cho máy Mac sử dụng các ký tự Ansi đầy màu sắc.

3、[upiano](https://github.com/eliasdorneles/upiano)

![](https://cdn.beekka.com/blogimg/asset/202308/bg2023081012.webp)

Mô phỏng tiếng đàn piano ngay trong dòng lệnh.

4、[WSL Distro Manager](https://github.com/bostrot/wsl2-distro-manager)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031207.webp)

Giao diện đồ họa giúp bạn quản lý các bản phân phối Linux trên Windows (WSL) một cách dễ dàng hơn.

5、[Mole](https://github.com/tw93/Mole)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031213.webp)

Công cụ dọn dẹp và tối ưu hóa mã nguồn mở dành cho macOS.

6、[PipeGate](https://github.com/janbjorge/pipegate)

Công cụ tạo đường hầm ánh xạ dịch vụ nội bộ ra ngoài internet, sử dụng các script Python đơn giản và hỗ trợ xác thực UUID.

7、[HookListener](https://www.hooklistener.com)

![](https://cdn.beekka.com/blogimg/asset/202412/bg2024121804.webp)

Công cụ trực tuyến để quản lý và kiểm thử Webhook, cho phép sử dụng miễn phí cá nhân.

8、[Sentinel](https://github.com/suzuran0y/CCTV-Smartphone-AI-Monitoring)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031201.webp)

Biến điện thoại Android cũ thành camera an ninh thông minh tích hợp AI. ([@suzuran0](https://github.com/ruanyf/weekly/issues/9201) đóng góp)

9、[Flux Monitor](https://github.com/chentao1006/FluxMonitor)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031203.webp)

Bảng theo dõi và quản lý hệ thống dành cho người dùng Mac. ([@chentao1006](https://github.com/ruanyf/weekly/issues/9207) đóng góp)

## AI liên quan

1、[Agentic Metric](https://github.com/MrQianjinsi/agentic-metric)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030603.webp)

Công cụ dòng lệnh Python để theo dõi mức độ sử dụng của các coding agent nội bộ (như Claude Code, Codex). ([@MrQianjinsi](https://github.com/ruanyf/weekly/issues/9165) đóng góp)

2、[cc-connect](https://github.com/chenhg5/cc-connect)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031202.webp)

Cầu nối mã nguồn mở giúp kết nối các công cụ lập trình AI với ứng dụng nhắn tin trên điện thoại. ([@chenhg5](https://github.com/ruanyf/weekly/issues/9202) đóng góp)

3、[Page Agent](https://github.com/alibaba/page-agent)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030702.webp)

Chèn thư viện JS này vào trang web để điều khiển trang bằng ngôn ngữ tự nhiên.

4、[Agent Safehouse](https://github.com/eugene1g/agent-safehouse)

Công cụ sandbox cho macOS dùng để chạy các công cụ lập trình AI một cách an toàn.

5、[Repo Tokens](https://github.com/qwibitai/nanoclaw/tree/main/repo-tokens)

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022801.webp)

GitHub Action hiển thị quy mô kho lưu trữ dưới dạng số lượng Token mà một mô hình AI cần để xử lý.

## Tài nguyên

1、[Theo dõi thế giới](https://www.worldmonitor.app) (World Monitor)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030801.webp)

Một bảng tin thời gian thực tổng hợp các nguồn tin tức quan trọng trên thế giới.

2、[Khám phá nhà máy lọc dầu](https://fuelingcuriosity.com/game.html)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031204.webp)

Trang web tương tác minh họa quá trình nhà máy lọc dầu biến dầu thô thành xăng và dầu diesel.

3、[Mechanical Pencil](https://mechanical-pencil.com)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031001.webp)

Các hoạt ảnh về cơ cấu máy móc của các vật dụng đời thường như bút bi, bật lửa.

## Hình ảnh

1、[Phương pháp thay thế mật khẩu](https://tesseral.com/blog/i-designed-some-more-user-friendly-methods-for-multi-factor-authentication)

Một lập trình viên đã phát minh ra cách đăng nhập mới bằng bộ bài Tây.

Hệ thống cho bạn chọn 5 lá bài từ bộ 52 lá theo một thứ tự nhất định làm mật khẩu.

![](https://cdn.beekka.com/blogimg/asset/202507/bg2025073110.webp)

Lần sau khi đăng nhập, bạn phải chọn đúng 5 lá bài đó theo đúng thứ tự.

## Văn trích

1、[Sự sụp đổ của những xã hội phức tạp](https://news.ycombinator.com/item?id=31670526)

Chúng ta đều biết khi một phần mềm trở nên quá phức tạp, nó sẽ rất khó bảo trì và cuối cùng thường bị từ bỏ.

Nhà sử học Joseph Tainter cho rằng xã hội loài người cũng vậy. Nếu độ phức tạp vượt quá giới hạn, xã hội đó rốt cuộc sẽ sụp đổ.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026031214.webp)

Năm 1988, ông xuất bản cuốn sách "Sự sụp đổ của những xã hội phức tạp", mô tả sự hưng thịnh và suy tàn của các nền văn minh như La Mã, Maya... để trả lời câu hỏi: **Tại sao những xã hội hùng mạnh lại sụp đổ?**

Ông cho rằng kẻ thù chính là sự phức tạp.

Khi nền văn minh phát triển, xã hội tăng thêm sự phức tạp: nhiều cấp bậc hơn, nhiều bộ máy quan liêu hơn. Ban đầu, chúng có ích (giúp tăng sản lượng, thuế...). Nhưng đến một lúc nào đó, quy luật hiệu suất giảm dần xuất hiện.

(1) Càng nhiều luật lệ và quan lại, chi phí chính phủ càng tăng, lâu dần xã hội không gánh nổi.

(2) Sự phức tạp làm tăng bất bình đẳng, vì càng ít người hiểu được mọi quy tắc, bạn càng lệ thuộc vào các luật sư.

(3) Càng nhiều quy tắc, bộ máy duy trì chúng càng phình to, làm giảm hiệu quả xã hội.

(4) Cuối cùng, sự phức tạp dẫn đến khoảng cách giàu nghèo và đối kháng giai cấp. Tổng hợp các yếu tố này dẫn đến sự tan rã cuối cùng.

## Trích dẫn

1\.

Năm 2021, tôi cảm thấy thật tuyệt vời khi làm một kỹ sư phần mềm. Ngành công nghiệp bùng nổ, cơ hội khắp nơi.

Năm 2026, tôi không chắc 10 năm nữa nghề này sẽ ra sao. Dù thế nào, cái công việc lập trình mà tôi hằng yêu quý sắp sửa biến mất rồi.

-- [Tôi không biết 10 năm nữa công việc của mình còn tồn tại không](https://www.seangoedecke.com/will-my-job-still-exist/)

2\.

Đối đầu với một AI mạnh mẽ mang lại cảm giác rất lạ: bạn thấy mình yếu đi một cách vô lý, còn AI thì làm gì cũng vượt ngoài mong đợi, hệt như bạn đang đấu với một tay chơi luôn có vận may mỉm cười trong mọi ván bài vậy.

-- [probablydance.com](https://probablydance.com/2026/03/07/im-getting-a-whiff-of-iain-banks-culture/)

3\.

Đọc sách kinh doanh đôi khi chỉ là lãng phí thời gian. Chúng biến những câu chuyện đơn giản thành lời khuyên vạn năng, biến thành công ngẫu nhiên thành chiến lược phổ quát, và thay thế thị trường phức tạp bằng những khẩu hiệu sáo rỗng.

-- [Đọc sách kinh doanh là lãng phí thời gian](https://antemedian.substack.com/p/why-reading-business-books-is-a-waste)

4\.

Thời gian là tài nguyên duy nhất không thể tái tạo. Với tôi, các gói thuê bao mô hình AI hiện nay là cách rẻ nhất để mua thêm thời gian cho chính mình.

-- [Đừng quá khắt khe với phí thuê bao AI](https://steipete.me/posts/2025/stop-overthinking-ai-subscriptions)

(Hết)
