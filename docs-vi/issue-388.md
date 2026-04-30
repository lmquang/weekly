# Kiểm thử chính là pháo đài mới

Bản tin này ghi lại những nội dung công nghệ đáng chia sẻ hàng tuần, phát hành vào thứ Sáu.

Tạp chí này [mã nguồn mở](https://github.com/ruanyf/weekly), hoan nghênh bạn [đóng góp](https://github.com/ruanyf/weekly/issues). Ngoài ra còn có dịch vụ ["Ai đang tuyển dụng"](https://github.com/ruanyf/weekly/issues/9088) dành cho các lập trình viên. Nếu muốn hợp tác, bạn hãy [liên hệ qua email](mailto:yifeng.ruan@gmail.com) (yifeng.ruan@gmail.com) nhé.

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026030804.webp)

Tại một khu thắng cảnh ở Phù Lăng, Trùng Khánh, người ta vừa khánh thành chiếc "cầu treo cự thạch" đầu tiên trên thế giới. Mặt cầu được ghép từ những tảng đá khổng lồ, chỉ cần một phút lơ là bạn có thể bước hụt bất cứ lúc nào. ([via](https://www.cbg.cn/a/77561/20260214/7b37135efeb74f0fbbaf272a9b7f6ae0.html))

## Kiểm thử chính là pháo đài mới

[Next.js](https://nextjs.org) hiện đang là "ông vua" không thể chối cãi trong làng framework JS. Tôi đồ rằng phải đến một nửa số ứng dụng JS full-stack hiện nay được xây dựng dựa trên nền tảng này.

Thế nhưng, chỉ cách đây hai tuần, một tin tức chấn động đã làm lung lay vị thế của gã khổng lồ này.

Một kỹ sư tại Cloudflare vừa [tuyên bố](https://blog.cloudflare.com/vinext/) rằng anh ta đã **tái hiện thành công toàn bộ Next.js chỉ trong đúng một tuần bằng AI**, và đặt tên cho nó là [vinext](https://vinext.io/).

Thực tế, bản mẫu sản phẩm đã ra đời ngay trong ngày đầu tiên, những ngày sau đó chỉ là để tinh chỉnh thêm.

> "Tôi thực sự bắt tay vào làm từ ngày 13 tháng 2. Ngay tối hôm đó, các tính năng cơ bản đã xong xuôi. Chiều hôm sau, 10 trên tổng số 11 bộ định tuyến (router) đã sẵn sàng. Đến ngày thứ ba, nó đã được deploy lên server của chúng tôi với khả năng hydrate hoàn chỉnh ở phía client. Những ngày kế tiếp, tôi tập trung gia cố bảo mật: xử lý các trường hợp biên, mở rộng bộ kiểm thử, đưa tỷ lệ bao phủ API lên tới 94%."

Đáng kinh ngạc hơn, bản tái hiện này còn có hiệu năng vượt trội so với bản gốc.

> "Các bài kiểm tra benchmark sớm cho thấy tốc độ build nhanh gấp 4 lần, dung lượng gói bundle cho client giảm tới 57%. Thậm chí, một số ứng dụng Next.js thực tế đã có thể chạy trực tiếp trên nền tảng mới này."

Hiện mã nguồn của vinext đã được [công khai](https://github.com/cloudflare/vinext).

Tôi cho rằng đây là một cú giáng cực mạnh vào Next.js. Next.js là sản phẩm chủ lực của Vercel với đội ngũ phát triển hùng hậu và nguồn vốn đầu tư khổng lồ suốt 10 năm qua. Dù là mã nguồn mở, nhưng họ thu lợi từ bản Enterprise, các dịch vụ đám mây, plugin và giao diện, mang về doanh thu tới 200 triệu USD vào năm ngoái.

**Cái gọi là "pháo đài công nghệ" tưởng chừng bất khả xâm phạm đó giờ đây bỗng trở nên mỏng manh trước AI**. Một kỹ sư đơn độc chỉ mất một tuần để sao chép thành quả của cả một tập đoàn trong một thập kỷ. Các ứng dụng hiện tại thậm chí chẳng cần sửa một dòng code nào vẫn có thể chạy ngon lành trên bản tái hiện.

Bạn có biết chi phí cho việc này là bao nhiêu không? Chỉ vỏn vẹn 1.100 USD tiền Token AI!

Điều này khiến Vercel lâm vào thế khó: làm sao để tiếp tục đổ tiền vào phát triển Next.js khi khách hàng giờ đây chẳng còn mặn mà trả phí cao cho những tính năng có thể dễ dàng bị sao chép.

Nhìn rộng ra, mọi phần mềm thương mại đều đang đứng trước nguy cơ bị đe dọa. **Rào cản về mã nguồn đã không còn tồn tại. Chỉ với một khoản đầu tư nhỏ, AI có thể tái hiện bất kỳ phần mềm phức tạp nào.**

Vậy để tự bảo vệ mình, các công ty phần mềm sẽ làm gì? **Câu trả lời nằm ở các bộ kiểm thử (test cases).**

Lý do chính giúp kỹ sư Cloudflare tái hiện thành công Next.js là vì dự án này có hệ thống tài liệu quá tốt và bộ test cases cực kỳ đầy đủ. AI chỉ cần mô phỏng từng API và chạy thử với bộ test gốc, nếu vượt qua thì coi như đã tương thích 100%.

Nếu không có bộ test cases đó, chẳng ai dám chắc code AI viết ra có chạy đúng như kỳ bản gốc hay không, và đương nhiên không ai dám đưa nó vào môi trường thực tế.

Chúng ta có thể dự đoán rằng sắp tới, các dự án phần mềm lớn sẽ bảo mật bộ test cases của mình như một tài sản vô giá. **Kiểm thử mới chính là pháo đài thực sự.**

Hãy nhìn vào [SQLite](https://sqlite.org), cơ sở dữ liệu phổ biến nhất thế giới. Mã nguồn của nó chỉ có 156.000 dòng, nhưng bộ test cases lên tới [92,05 triệu dòng](https://sqlite.org/testing.html) - gấp 590 lần! Trong đó, bộ kiểm thử cốt lõi [TH3](https://sqlite.org/th3.html) hoàn toàn đóng nguồn. Nó dùng để kiểm tra các tình huống cực đoan trong ngành hàng không, y tế... Chính những bộ test bảo mật này đã khiến SQLite gần như không thể bị sao chép hoàn hảo.

Gần đây, dự án mã nguồn mở [tldraw](https://github.com/tldraw/tldraw/issues/8082) cũng đã có động thái tương tự khi chuẩn bị đóng mã nguồn các bộ kiểm thử.

Thú thực, việc bảo mật test cases không có lợi cho sự phát triển chung của cộng đồng mã nguồn mở, nhưng các nhà phát triển buộc phải làm vậy để bảo vệ thành quả của mình trước sức mạnh ngày càng đáng sợ của AI.

## Vấn đề bản quyền khi AI tái hiện phần mềm

Việc AI "xào" lại phần mềm cũng đang gây ra [nhiều tranh cãi](https://tuananh.net/2026/03/05/relicensing-with-ai-assisted-rewrite/) về mặt pháp lý.

Next.js sử dụng giấy phép MIT rất thông thoáng nên việc tái hiện không gặp vấn đề bản quyền. Tuy nhiên, một dự án khác mang tên [chardet](https://github.com/chardet/chardet) bị tái hiện và đổi từ giấy phép LGPL sang MIT đã khiến tác giả gốc vô cùng phẫn nộ.

Cộng đồng mạng hiện đang chia làm hai phe:
- Phe ủng hộ cho rằng AI chỉ tái hiện chức năng và giao diện API, còn mã nguồn bên trong hoàn toàn khác biệt, nên việc đổi giấy phép là hợp lệ.
- Phe phản đối lập luận rằng theo quy định của GPL, mọi sản phẩm phái sinh đều không được phép đổi giấy phép, và bản tái hiện AI rõ ràng là một sản phẩm phái sinh.

Mọi chuyện còn rắc rối hơn khi luật pháp Mỹ hiện quy định các sản phẩm do AI tạo ra không có bản quyền và thuộc về cộng đồng. Điều này đồng nghĩa với việc **các phần mềm do AI tái hiện sẽ không thể áp dụng bất kỳ giấy phép nào, vì chúng vốn dĩ không có bản quyền ngay từ đầu.**

Nếu tiền lệ này được thiết lập, các loại giấy phép phần mềm sẽ trở nên vô nghĩa. Bất kể bạn dùng giấy phép gì, người khác chỉ cần dùng AI tái hiện lại là có thể lách luật một cách hợp pháp.

## Tin công nghệ

1. [AI chỉnh sửa lời lẽ thô tục](https://decrypt.co/360183/roblox-using-ai-rewrite-chat-swears-slurs-real-time)

Nền tảng game Roblox vừa [thông báo](https://ir.roblox.com/news/news-details/2026/Roblox-Launches-Real-Time-Chat-Rephrasing-to-Maintain-Civility-and-Gameplay-Flow/default.aspx) sẽ dùng AI để chỉnh sửa trực tiếp các cuộc đối thoại của game thủ nhằm hướng tới một môi trường văn minh hơn. Thay vì chỉ che đi bằng các ký hiệu `####`, AI sẽ viết lại cả câu nói sao cho lịch sự mà vẫn giữ được ý nghĩa, khiến người nghe thậm chí không nhận ra đối phương đang định văng tục. Dù có phần hơi "giả trân", nhưng đây là một nỗ lực cần thiết để bảo vệ bầu không khí trên các diễn đàn mạng.

2. [Internet bằng laser trên máy bay](https://www.esa.int/Applications/Connectivity_and_Secure_Communications/World-first_gigabit-per-second_laser_link_between_aircraft_and_geostationary_satellite)

Cơ quan Vũ trụ Châu Âu (ESA) vừa thử nghiệm thành công việc kết nối internet tốc độ cao cho máy bay thông qua laser. Thay vì dùng sóng vô tuyến như Starlink, laser mang lại băng thông cực lớn và không bị hạn chế bởi tần số vô tuyến. Tốc độ đạt được lên tới 2,6Gbps, nhanh gấp 8 đến 10 lần so với hiện nay. Điểm yếu duy nhất là laser yêu cầu một đường truyền thẳng tắp, không bị mây che khuất, nên có lẽ chỉ phát huy tác dụng tốt nhất khi máy bay đã lên tới độ cao nhất định.

3. [Bản sao kỹ thuật số của các chuyên gia trên Grammarly](https://www.theverge.com/ai-artificial-intelligence/890921/grammarly-ai-expert-reviews)

Tính năng "Ý kiến chuyên gia" của Grammarly vừa gây sốc khi một người dùng phát hiện ra sếp cũ của mình (đã qua đời) lại xuất hiện trong danh sách chuyên gia tư vấn. Hóa ra, Grammarly đã dùng AI để tạo ra các "phân thân kỹ thuật số" dựa trên bài viết của các chuyên gia thật để nhận xét bài viết cho người dùng. Điều này đặt ra một dấu hỏi lớn về đạo đức: chúng ta có quyền "hồi sinh" ai đó dưới dạng kỹ thuật số để phục vụ mục đích thương mại hay không?

4. [Hòm thư năng lượng mặt trời](https://www.bbc.com/news/articles/cgln72rgrero)

Khi thư tay dần biến mất, Bưu điện Hoàng gia Anh đã có một bước đi sáng tạo: biến 3.500 hòm thư truyền thống thành "hòm thư năng lượng mặt trời". Phần mái được lắp tấm pin quang điện, và chức năng cũng chuyển từ nhận thư sang nhận gửi các bưu kiện nhỏ. Cách làm này vừa bảo tồn được nét văn hóa đặc trưng của những hòm thư đỏ, vừa đáp ứng nhu cầu thực tế của thời đại thương mại điện tử.

## Bài viết hay

1. [Cuộc tấn công "tiêm Prompt" qua tiêu đề Issue trên GitHub](https://grith.ai/blog/clinejection-when-your-ai-tool-installs-another) (Tiếng Anh)

Một lỗ hổng bảo mật thú vị khi hacker chèn mã độc vào tiêu đề Issue để đánh lừa các công cụ AI đang thực hiện phân loại, từ đó chiếm đoạt token và phát hành các phiên bản phần mềm độc hại.

2. [Đánh giá lại giá trị của file AGENTS.md](https://www.infoq.com/news/2026/03/agents-context-file-value-review/) (Tiếng Anh)

Nghiên cứu mới chỉ ra rằng file AGENTS.md đôi khi lại gây tác dụng ngược khi khiến mô hình AI phải "suy nghĩ" quá nhiều, làm tăng chi phí nhưng lại làm giảm chất lượng mã nguồn tạo ra.

3. [Hành trình 9 năm của Temporal API](https://bloomberg.github.io/js-blog/post/temporal/) (Tiếng Anh)

Temporal API cuối cùng đã chính thức trở thành một phần của tiêu chuẩn ES2026. Bài viết nhìn lại chặng đường gian nan để đưa một cú pháp mới vào JavaScript.

4. [Bài test khả năng "nói phét" của AI](https://decrypt.co/360596/benchmark-test-measures-ai-bullshit-most-models-fail) (Tiếng Anh)

BullshitBench là một bộ câu hỏi đặc biệt để kiểm tra xem liệu AI có đủ thông minh để nhận ra những câu hỏi vô nghĩa, hay vẫn cố gắng trả lời một cách cực kỳ nghiêm túc.

5. [CSS thuần là đủ rồi](https://www.zolkos.com/2025/12/03/vanilla-css-is-all-you-need) (Tiếng Anh)

37Signals chứng minh rằng bạn hoàn toàn có thể xây dựng những hệ thống lớn mà không cần đến Tailwind hay Sass, chỉ với sức mạnh của CSS nguyên bản.

6. [Vật lý học về... việc đi ngoài](https://theconversation.com/physics-of-poo-why-it-takes-you-and-an-elephant-the-same-amount-of-time-76696) (Tiếng Anh)

Một bài viết khoa học có phần kỳ quặc giải thích tại sao hầu hết các loài động vật có vú, từ chuột đến voi, đều có thời gian đi vệ sinh trung bình khoảng 12 giây.

## Công cụ

1. [KULA](https://github.com/c0m4r/kula)

Công cụ giám sát server Linux siêu nhẹ chỉ với một file thực thi duy nhất.

2. [WSL Distro Manager](https://github.com/bostrot/wsl2-distro-manager)

Giao diện đồ họa giúp bạn quản lý các bản phân phối Linux trên Windows (WSL) một cách dễ dàng hơn.

3. [Mole](https://github.com/tw93/Mole)

Dọn dẹp và tối ưu hóa hệ điều hành macOS với bộ công cụ mã nguồn mở.

4. [Sentinel](https://github.com/suzuran0y/CCTV-Smartphone-AI-Monitoring)

Tận dụng những chiếc điện thoại Android cũ để làm camera an ninh tích hợp AI. ([@suzuran0](https://github.com/ruanyf/weekly/issues/9201) đóng góp)

5. [Flux Monitor](https://github.com/chentao1006/FluxMonitor)

Bảng theo dõi trạng thái hệ thống cho người dùng Mac. ([@chentao1006](https://github.com/ruanyf/weekly/issues/9207) đóng góp)

## AI liên quan

1. [Agentic Metric](https://github.com/MrQianjinsi/agentic-metric)

Theo dõi lượng Token và chi phí sử dụng của các công cụ lập trình AI Agent trên máy bạn. ([@MrQianjinsi](https://github.com/ruanyf/weekly/issues/9165) đóng góp)

2. [cc-connect](https://github.com/chenhg5/cc-connect)

Cầu nối giúp bạn điều khiển các công cụ lập trình AI trực tiếp qua các ứng dụng nhắn tin trên điện thoại. ([@chenhg5](https://github.com/ruanyf/weekly/issues/9202) đóng góp)

3. [Page Agent](https://github.com/alibaba/page-agent)

Thư viện JS cho phép bạn điều khiển trang web bằng ngôn ngữ tự nhiên: "Hãy tóm tắt nội dung tài liệu trong menu điều hướng cho tôi".

4. [Repo Tokens](https://github.com/qwibitai/nanoclaw/tree/main/repo-tokens)

GitHub Action giúp hiển thị quy mô của một kho lưu trữ dưới dạng số lượng Token mà một mô hình AI cần để xử lý.

## Văn trích

1. [Sự sụp đổ của những xã hội phức tạp](https://news.ycombinator.com/item?id=31670526)

Tương tự như một phần mềm khi trở nên quá phức tạp sẽ không thể bảo trì, các xã hội loài người cũng có thể sụp đổ nếu độ phức tạp vượt quá giới hạn chịu đựng. Nhà sử học Joseph Tainter trong cuốn sách cùng tên đã chỉ ra rằng: ban đầu sự phức tạp (các tầng lớp xã hội, cơ quan công quyền) giúp tăng năng suất, nhưng đến một ngưỡng nào đó, cái giá phải trả để duy trì sự phức tạp đó sẽ lớn hơn cả lợi ích nó mang lại. Kết quả là xã hội trở nên bất bình đẳng, kém hiệu quả và cuối cùng là tan rã.

## Trích dẫn

1.

Năm 2021, tôi cảm thấy thật tuyệt vời khi làm một kỹ sư phần mềm. Năm 2026, tôi chẳng còn chắc 10 năm nữa cái nghề này sẽ ra sao. Dù thế nào đi nữa, cái công việc lập trình mà tôi hằng yêu quý sắp sửa biến mất rồi.

-- Trích "Tôi không biết liệu 10 năm nữa công việc của mình còn tồn tại"

2.

Đối đầu với một AI mạnh mẽ mang lại cảm giác rất lạ: bạn thấy mình yếu đi một cách vô lý, còn AI thì làm gì cũng vượt ngoài mong đợi, hệt như bạn đang đấu với một tay chơi luôn có vận may mỉm cười trong mọi ván bài vậy.

-- probablydance.com

3.

Đọc sách kinh doanh đôi khi chỉ là lãng phí thời gian. Chúng biến những câu chuyện thành công ngẫu nhiên thành những công thức vạn năng và thay thế sự phức tạp của thị trường bằng những khẩu hiệu sáo rỗng.

-- Đọc sách kinh doanh là lãng phí thời gian

4.

Thời gian là tài nguyên duy nhất không thể tái tạo. Với tôi, các gói thuê bao mô hình AI hiện nay là cách rẻ nhất để mua thêm thời gian cho chính mình.

-- Đừng quá khắt khe với phí thuê bao AI

## Nhìn lại năm xưa

[Lập trình Low-code có lẽ sẽ khó thành công](https://www.ruanyifeng.com/blog/2025/03/weekly-issue-341.html) (#341)

[AI không có pháo đài ngăn cách](http://www.ruanyifeng.com/blog/2024/03/weekly-issue-291.html) (#291)

[Động lực tăng trưởng của Trung Quốc nằm ở vùng nội địa](http://www.ruanyifeng.com/blog/2023/02/weekly-issue-241.html) (#241)

[Con đường tự do tài chính của một lập trình viên](http://www.ruanyifeng.com/blog/2022/01/weekly-issue-191.html) (#191)

(Hết)
