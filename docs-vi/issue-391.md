# Sự phân hóa giàu nghèo của AI

Bản tin này ghi lại những nội dung công nghệ đáng chia sẻ hàng tuần, phát hành vào thứ Sáu.

Tạp chí này [mã nguồn mở](https://github.com/ruanyf/weekly), hoan nghênh [đóng góp](https://github.com/ruanyf/weekly/issues). Ngoài ra còn có dịch vụ ["Ai đang tuyển dụng"](https://github.com/ruanyf/weekly/issues/9454), đăng tin tuyển dụng lập trình viên. Hợp tác vui lòng [liên hệ qua email](mailto:yifeng.ruan@gmail.com) (yifeng.ruan@gmail.com).

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040107.webp)

Trang trí tường tại một nhà hàng ở Thượng Hải. (via [monana3838@Threads](https://www.threads.com/@monana3838/post/DWjVcmcAoh4))

## Sự phân hóa giàu nghèo của AI

Tôi ngày càng cảm thấy AI không giống như các công nghệ khác. Nó không chỉ mang lại cuộc cách mạng kỹ thuật mà còn mang lại sự thay đổi xã hội.

Nói đơn giản là AI sẽ gây ra sự phân hóa giàu nghèo.

Các công nghệ khác thực tế lại xóa bỏ sự phân hóa này và thực hiện "bình đẳng người tiêu dùng". Nghĩa là người nghèo và người giàu tiêu dùng những thứ giống nhau.

Ví dụ, mọi người uống cùng một loại Coca-Cola, dùng cùng một loại iPhone, lái cùng một chiếc Tesla. Thậm chí Internet cũng vậy, người giàu nhất thế giới Elon Musk dùng cùng một trang web và ứng dụng điện thoại giống hệt bạn.

Nhưng các mô hình AI thì không phải vậy. **Trước các mô hình lớn, người nghèo và người giàu không bình đẳng**.

Trong tương lai, người bình thường chắc chắn sẽ không dùng nổi các mô hình lớn hàng đầu. Thực tế thì hiện giờ đã như vậy rồi. Gói lập trình AI đắt nhất là gói Max của Claude Code với phí tháng 200 USD, nhiều người đã không còn gánh nổi.

OpenAI từng hình dung về [gói phí 20.000 USD một tháng](https://www.thepaper.cn/newsDetail_forward_30320495) để cung cấp dịch vụ mô hình lớn nhất và không giới hạn.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032207.webp)

Nếu thực sự ra mắt, chỉ giới siêu giàu mới dùng nổi.

Điều này phản ánh một sự thật đơn giản là **phí càng đắt, hiệu quả mô hình càng tốt**. Bởi vì hiệu quả của mô hình liên quan đến năng lực tính toán. Nhiều năng lực tính toán hơn, ngữ cảnh lớn hơn, tham số nhiều hơn đều cần tiền.

Điều này hoàn toàn ngược lại với các sản phẩm công nghiệp. Hàng công nghiệp có hiệu ứng quy mô, sản lượng càng cao thì giá thành đơn vị càng thấp. Một khi sản xuất quy mô lớn, giá cả sẽ ngày càng rẻ.

Tuy nhiên, **mô hình lớn không có hiệu ứng quy mô**. Việc sản xuất quy mô lớn các mô hình cần nhiều máy chủ hơn, điều này không làm giảm chi phí đơn vị. Ngược lại, nó có thể trở nên đắt hơn vì phải xây thêm phòng máy, cải tạo hệ thống điện nước.

Xã hội tương lai có lẽ sẽ thế này: Người giàu và người nghèo dùng các mô hình khác nhau. Các dịch vụ của mô hình hàng đầu như lập kế hoạch, tư vấn, tạo nội dung, tự động hóa sẽ cần trả phí sử dụng cắt cổ. Còn người bình thường sẽ dùng các mô hình miễn phí, và hiệu quả tất nhiên cũng rất bình thường.

Nhưng tôi cũng thấy Elon Musk [gần đây nói rằng](https://wap.cj.sina.cn/7x24/4762771), tương lai còn một khả năng khác.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032206.webp)

Ý ông ấy là năng lực tính toán về bản chất là một hình thức chuyển hóa năng lượng. Con người cuối cùng sẽ đạt được nguồn cung năng lượng rẻ và dồi dào (như năng lượng mặt trời trong không gian chẳng hạn). Vì vậy năng lực tính toán sẽ trở nên đủ rẻ để tất cả mọi người đều được dùng những mô hình tốt nhất.

Có khả năng không? Tôi không biết, nhưng cảm thấy trường hợp đầu tiên thực tế hơn.

## Một phương pháp đo lường năng lực mô hình

Làm sao để đo lường năng lực của một mô hình lớn?

Cách hiện nay là sử dụng một bộ kiểm tra để tính điểm. Nhược điểm của nó là chỉ dùng để so sánh ngang hàng, rất khó đo lường tốc độ tiến bộ.

Gần đây, một bài báo đã đề xuất [một phương pháp đo lường mới](https://emptysqua.re/blog/review-measuring-ai-ability-to-complete-long-software-tasks/).

Các nhà khoa học đầu tiên tính toán xem con người cần bao nhiêu thời gian để hoàn thành một nhiệm vụ cụ thể. Ví dụ, tính 4 + 5 + 7 mất 2 giây, còn tính 37 * 52 * 19 có thể mất 1 phút.

Sau đó, họ kiểm tra xem mô hình lớn có thể hoàn thành nhiệm vụ đó với tỷ lệ thành công 50% hay không.

Nghiên cứu phát hiện ra rằng, các nhiệm vụ mà GPT-2 hoàn thành với tỷ lệ thành công 50% nằm trong khoảng 2 giây. Claude 3.7 Sonnet là 50 phút. O3 gần 2 tiếng. Opus 4.6 khoảng 12 tiếng.

Nghĩa là nhiệm vụ mà con người cần 12 tiếng mới hoàn thành thì Opus 4.6 có xác suất thành công là 50%.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040201.webp)

Kết quả là hình trên. Có thể thấy tốc độ tiến hóa của mô hình lớn là một đường thẳng trong hệ tọa độ logarit.

**Cứ sau mỗi 7 tháng, khoảng thời gian của nhiệm vụ mà mô hình lớn hoàn thành với tỷ lệ thành công 50% lại tăng gấp đôi**. Theo xu hướng này, mô hình lớn sẽ hoàn thành nhiệm vụ mà một chuyên gia con người cần một tháng mới làm xong với tỷ lệ thành công 50% trong khoảng từ năm 2027 đến 2031.

Nếu bài báo này đúng, nó có nghĩa là các mô hình ra mắt vào cuối năm sẽ mạnh gấp đôi so với đầu năm.

## Tin công nghệ

1、[Trứng phục sinh trong điều khoản người dùng](https://www.cape.co/blog/easter-egg-in-privacy-policy)

Điều khoản người dùng của các dịch vụ phần mềm thường vừa dài vừa khó hiểu, rất ít người đọc, nhưng bên trong lại chứa nhiều nội dung quan trọng.

Một nhà mạng viễn thông Mỹ, để chứng tỏ mình rất coi trọng quyền lợi người dùng, đã khuyến khích mọi người đọc "Điều khoản người dùng" bằng cách bí mật thêm vào một quả trứng phục sinh.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026033101.webp)

Câu được bôi đậm trong hình trên viết: "Nếu bạn đọc được câu này, hãy gửi email đến hòm thư của chúng tôi để nhận một chuyến du lịch Thụy Sĩ miễn phí."

Sau khi triển khai hai tuần mới có người gửi email hỏi xem chuyện này có thật không. Vì chỉ có đúng một người gửi nên cô ấy đã được đi Thụy Sĩ miễn phí.

Qua chuyện này có thể thấy, ngay cả khi có trứng phục sinh thì cũng chẳng ai đọc "Điều khoản người dùng". Cách làm của tôi hiện nay là nhờ mô hình lớn giúp đỡ, hỏi rằng "thỏa thuận này có những điểm nào bất lợi cho người dùng", và kết quả là nhận được câu trả lời rất nhanh.

2、[Sơn móng tay cảm ứng](https://www.livescience.com/chemistry/chemistry-student-develops-clear-polish-that-turns-your-fingernail-into-a-touch-screen-stylus)

Màn hình cảm ứng điện dung được sử dụng rộng rãi có một vấn đề là sẽ mất tác dụng nếu đeo găng tay.

Nguyên nhân là nó yêu cầu vật chạm vào (như ngón tay) phải dẫn điện để màn hình tạo ra sự nhiễu loạn điện trường, từ đó xác định vị trí chạm.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032802.webp)

Cách giải quyết cũng đơn giản là bôi một lớp sơn móng tay lên đầu ngón tay của găng tay. Các mảnh vụn kim loại trong sơn móng tay có thể dẫn điện.

Một sinh viên đại học ngành hóa học ở Mỹ, khi học về hóa học mỹ phẩm, đã phát minh ra một loại sơn móng tay trong suốt cải tiến chuyên dùng để sử dụng màn hình cảm ứng khi đeo găng tay.

Loại sơn này trong suốt, bôi lên găng tay sẽ không nhìn thấy, cũng có thể bôi lên móng tay thật để làm chất đánh bóng.

3、[Quảng cáo của Copilot](https://www.theregister.com/2026/03/30/github_copilot_ads_pull_requests/)

Copilot là trợ lý AI do GitHub ra mắt. Tuần trước, một số người dùng phát hiện nó tự động chèn quảng cáo.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040106.webp)

Hình trên là [một Pull Request](https://github.com/rab781/RabTradebot/pull/77) do Copilot tự động gửi. Nó đã thêm một quảng cáo ở cuối phần mô tả (chỗ khoanh đỏ) để giới thiệu ứng dụng Raycast.

[Tìm kiếm một chút](https://github.com/search?q=%22%E2%9A%A1+Quickly+spin+up+copilot+coding+tasks%22&type=pullrequests) trên GitHub, bạn sẽ thấy đã có hơn 11.400 PR chứa cùng một lời quảng cáo này.

Sau khi bị người dùng phản đối, GitHub đã tạm dừng tính năng này. Nhưng đây là một tín hiệu nguy hiểm, cho thấy GitHub muốn tận dụng người dùng để tăng doanh thu.

## Bài viết

1、[Đánh giá Xiaomi MiMo v2 Pro](https://decrypt.co/362633/xiaomi-mimo-v2-pro-review-so-good-mistaken-deepseek-v4) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026033002.webp)

Xiaomi đã ra mắt dòng mô hình lớn MiMo V2. Đây là bài đánh giá của truyền thông nước ngoài với những lời khen ngợi rất cao.

2、[Tôi dùng AI để tạo ra một JavaScript engine](https://p.ocmatos.com/blog/jsse-a-javascript-engine-built-by-an-agent.html) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040105.webp)

Tác giả đã dùng 6 tuần để tạo ra một JavaScript engine vượt qua 100% bộ kiểm tra test262, bao quát toàn bộ 98.426 kịch bản. Bài viết này giới thiệu về quá trình đó.

3、[Giải phẫu thư mục .claude/](https://blog.dailydoseofds.com/p/anatomy-of-the-claude-folder) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026033114.webp)

Claude Code sẽ tạo ra thư mục con .claude/, nơi chứa tất cả dữ liệu lớp dưới do AI xử lý. Bài viết này nghiên cứu xem thư mục đó thực sự có gì.

4、[Giới thiệu về Consistent Hashing](https://eli.thegreenplace.net/2025/consistent-hashing) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102001.webp)

Consistent hashing là một thuật toán định vị bộ nhớ đệm. Trong trường hợp tăng hoặc giảm máy chủ bộ nhớ đệm, nó có thể không làm thay đổi vị trí ban đầu của bộ nhớ đệm đó.

5、 [Cách dùng laptop làm màn hình HDMI cho máy tính đơn bo](https://danielmangum.com/posts/laptop-hdmi-monitor-sbc/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025101009.webp)

Tác giả sử dụng một thẻ thu tín hiệu (capture card) chuyển đổi HDMI sang USB để biến laptop thành màn hình cho Raspberry Pi.

## Công cụ

1、[EmDash](https://github.com/emdash-cms/emdash)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040202.webp)

Một bản sao WordPress do AI tạo ra, dựa trên ngôn ngữ TypeScript, hỗ trợ plugin. Nghe nói các tính năng cơ bản giống hệt nhau, xem thêm tại [bài giới thiệu](https://blog.cloudflare.com/emdash-wordpress/).

2、[SubsTracker](https://github.com/wangwangit/SubsTracker)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032706.webp)

Hệ thống quản lý đăng ký thuê bao dựa trên Cloudflare Workers, có thể gửi thông báo hết hạn qua Telegram, Webhook. ([@wangwangit](https://github.com/ruanyf/weekly/issues/9411) đóng góp)

3、[OpeniLink Hub](https://github.com/openilink/openilink-hub)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032705.webp)

Nền tảng quản lý tin nhắn robot WeChat mã nguồn mở, có sẵn chợ ứng dụng để thêm tính năng cho bot qua vài cú nhấp chuột. ([@xixihhhh](https://github.com/ruanyf/weekly/issues/9404) đóng góp)

Ngoài ra còn một dự án tương tự là [wxWebHook](https://github.com/aristorechina/wxWebHook), gửi tin nhắn cho người dùng WeChat qua WebHook. ([@aristorechina](https://github.com/ruanyf/weekly/issues/9412) đóng góp)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032707.webp)

4、[Lixian.Online](https://lixian.online/)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026033115.webp)

Công cụ lấy gói cài đặt ngoại tuyến cho plugin VSCode, extension Chrome và ảnh Docker. [Mã nguồn mở](https://github.com/LiaoGuoYin/lixian.online). ([@LiaoGuoYin](https://github.com/ruanyf/weekly/issues/9455) đóng góp)

5、[Rename.Tools](https://rename.tools/zh/app)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026033116.webp)

Công cụ đổi tên tệp hàng loạt trên trình duyệt, hỗ trợ nhiều quy tắc cài đặt. [Mã nguồn mở](https://github.com/chenz24/rename.tools). ([@chenz24](https://github.com/ruanyf/weekly/issues/9461) đóng góp)

6、[FontInAss](https://github.com/Yuri-NagaSaki/FontInAss)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026033117.webp)

Công cụ tạo bộ font chữ con (subset) cho phụ đề mã nguồn mở, nhúng các ký tự cần thiết vào tệp phụ đề. ([@Yuri-NagaSaki](https://github.com/ruanyf/weekly/issues/9466) đóng góp)

7、[pretext.video](https://github.com/fifteen42/pretext-video)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040101.webp)

Một ứng dụng nhỏ dựa trên [Pretext](https://github.com/chenglou/pretext) (thư viện tính năng dàn trang văn bản), hiển thị đường nét cơ thể qua camera bằng văn bản theo thời gian thực. ([@fifteen42](https://github.com/ruanyf/weekly/issues/9472) đóng góp)

8、[OxideTerm](https://github.com/AnalyseDeCircuit/oxideterm)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040103.webp)

Trình cuối SSH đa nền tảng dựa trên Rust với nhiều tính năng, sử dụng framework Tauri. ([@AnalyseDeCircuit](https://github.com/ruanyf/weekly/issues/9474) đóng góp)

9、[wtree](https://github.com/FatDoge/wtree)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040104.webp)

Giao diện đồ họa để quản lý git worktree. ([@FatDoge](https://github.com/ruanyf/weekly/issues/9483) đóng góp)

## AI

1、[Open Agent SDK](https://github.com/shipany-ai/open-agent-sdk)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040102.webp)

Giải pháp thay thế mã nguồn mở cho claude-agent-sdk dựa trên mã nguồn Claude Code, dùng để phát triển AI Agent, hoàn toàn tương thích với giao diện gốc và không phụ thuộc vào tiến trình cli cục bộ. ([@idoubi](https://github.com/ruanyf/weekly/issues/9473) đóng góp)

2、[Antigravity Gateway](https://github.com/Truthan49/Antigravity-Everywhere)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032704.webp)

Bảng điều khiển Web quản lý thống nhất tất cả AI Agent cục bộ, hỗ trợ cách ly không gian làm việc, cộng tác từ xa qua Lark, hệ sinh thái Skills. ([@Mr-ZhangBo](https://github.com/ruanyf/weekly/issues/9395) đóng góp)

3、[ArcReel](https://github.com/ArcReel/ArcReel)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026032703.webp)

Trạm làm việc tạo video AI mã nguồn mở. Chỉ cần nhập một cuốn tiểu thuyết, nó sẽ tự động hoàn thành kịch bản, thiết kế nhân vật, phân cảnh và tạo video ngắn. ([@Pollo3470](https://github.com/ruanyf/weekly/issues/9393) đóng góp)

4、[TermCanvas](https://github.com/blueberrycongee/termcanvas)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026033001.webp)

Ứng dụng máy tính mã nguồn mở trải tất cả các terminal trên một khung vẽ vô hạn, thuận tiện để quản lý các công cụ lập trình AI. ([@blueberrycongee](https://github.com/ruanyf/weekly/issues/9434) đóng góp)

Ngoài ra còn một dự án tương tự là [OpenCove](https://github.com/DeadWaveWave/opencove). ([@DeadWaveWave](https://github.com/ruanyf/weekly/issues/9497) đóng góp)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040204.webp)

## Tài nguyên

1、[Hướng dẫn thực hành Claude Code](https://claude.nagdy.me/)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026033102.webp)

Hướng dẫn tương tác của Claude Code, giúp nắm vững công cụ lập trình AI này qua 11 bài tập nhỏ.

2、[Claude Code Unpacked](https://ccunpacked.dev/)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040108.webp)

Dựa trên mã nguồn Claude Code bị rò rỉ, trang web này minh họa từng bước cách phần mềm xử lý bên trong sau khi nhận được câu lệnh.

3、[Hướng dẫn nhập môn Machine Learning](https://github.com/dreddnafious/thereisnospoon/blob/main/ml-primer.md)

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026033108.webp)

Hướng dẫn học máy dành cho kỹ sư, giải thích các khái niệm cơ bản.

## Hình ảnh

1、[Cây của năm tại Châu Âu](https://nicenews.com/environment/european-tree-of-the-year-winners-2026/)

Châu Âu có một cuộc bình chọn "Cây của năm". Mới nghe thì thấy hơi lạ, nhưng nghĩ kỹ thì hoạt động này mang lại nhiều lợi ích như nâng cao danh tiếng thành phố, thúc đẩy bảo tồn sinh thái và du lịch.

Dưới đây là "Cây của năm" lần này.

Cây sồi ở làng Rukai, Litva, 400 năm tuổi.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026033103.webp)

Dưới đây là các cây khác lọt vào vòng chung kết.

Cây táo dại ở Slovakia.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026033104.webp)

Cây đu ở Ba Lan.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026033105.webp)

Cây bồ đề ở Latvia.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026033106.webp)

Cây bách ở Bồ Đào Nha.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026033107.webp)

## Điểm tin

1、[Càng dùng AI, tôi càng ít lo lắng](https://simonwillison.net/2025/Jul/4/identify-solve-verify/)

Tôi càng dành nhiều thời gian lập trình với AI thì càng ít lo lắng cho sự nghiệp của mình, ngay cả khi khả năng lập trình của AI ngày càng mạnh.

Bởi vì tôi nhận ra lập trình AI chỉ là một phần của quy trình, công việc của tôi không chỉ là viết mã.

Công việc thực sự của tôi là **tìm ra những vấn đề có thể giải quyết bằng mã, sau đó giải quyết chúng và xác minh xem giải pháp có hiệu quả không**.

AI cuối cùng có thể đảm nhận hoàn toàn phần viết mã ở giữa và hỗ trợ giải quyết phần đầu và phần cuối. Nhưng dù thế nào đi nữa, vẫn cần có người đi tìm vấn đề, định nghĩa vấn đề và xác nhận vấn đề đã được giải quyết.

Đó chính là 80% nội dung công việc của tôi.

2、[Sự không bền vững của Định luật Moore](https://bzolang.blog/p/the-unsustainability-of-moores-law)

Định luật Moore nói rằng cứ khoảng hai năm một lần, số lượng bóng bán dẫn trên một con chip sẽ tăng gấp đôi.

Nhưng nó còn một hiệu ứng đi kèm mà ít người nhắc đến. Đó là cứ khoảng năm năm một lần, chi phí xây dựng nhà máy sản xuất chip lại tăng gấp đôi, trong khi số lượng công ty chip có thể gánh vác chi phí đó lại giảm đi một nửa.

Hai mươi lăm năm trước, có khoảng 40 công ty có thể xây dựng nhà máy chip với chi phí mỗi nhà máy khoảng 2 đến 4 tỷ USD. Ngày nay, chỉ còn lại hai hoặc ba công ty (tùy vào việc bạn lạc quan thế nào về Intel) có thể xây dựng nhà máy chip tiên tiến nhất với chi phí vọt lên hàng chục tỷ USD.

Nếu xu hướng này tiếp tục trong 10 năm nữa, chi phí xây dựng nhà máy chip sẽ tiếp tục tăng gấp bội, có lẽ chỉ còn duy nhất một công ty hoặc không công ty nào gánh nổi.

Hiện tại, quy trình sản xuất chip đã tiến sát ngưỡng 1 nanomet. Nếu tiến xa hơn, rào cản kỹ thuật và rào cản tài chính sẽ đồng thời chạm đến giới hạn.

Tôi dự đoán Định luật Moore sẽ sớm mất hiệu lực. Tăng trưởng tương lai chủ yếu nằm ở năng lực tính toán tổng thể chứ không phải năng lực của một con chip đơn lẻ.

Các con chip trong tương lai sẽ giống như xe cũ, tốc độ chạy đều xấp xỉ nhau, chỉ khác ở độ mới cũ. Tôi thậm chí cảm thấy giữa con chip sản xuất năm 2035 và năm 2065 sẽ gần như không có sự khác biệt thực chất nào.

## Trích dẫn

1、

Việc tệp map của mã nguồn vô tình bị phát hành lên npm nghe có vẻ khó tin. Nhưng khi bạn nhận ra một phần lớn kho mã nguồn có lẽ được viết bởi chính AI mà bạn đang phát hành, mọi thứ sẽ trở nên dễ hiểu hơn.

-- [Bình luận của cư dân mạng](https://alex000kim.com/posts/2026-03-31-claude-code-source-leak/) về vụ rò rỉ mã nguồn Claude Code.

2、

Sự bùng nổ của trí tuệ nhân tạo khiến nhu cầu cho một số công việc văn phòng có thể không lớn, nhưng sẽ tạo ra một lượng lớn vị trí công việc cho thợ điện, thợ hàn và thợ sửa ống nước.

Trước đây, chúng ta bảo tất cả thanh niên đi học đại học để làm trong ngành ngân hàng, truyền thông hay luật pháp. Bây giờ cần cân bằng lại một chút. Một số người có lẽ phù hợp hơn để làm lao động chân tay. Trong các lĩnh vực như thợ sửa ống nước và thợ điện, sự nghiệp cũng có thể rất thành công.

-- [Larry Fink](https://www.bbc.com/news/articles/c9wqrdkx8ppo), ông chủ tập đoàn tài chính khổng lồ BlackRock của Mỹ.

3、

Mục đích của việc viết không phải là để viết xong, mà là để tăng cường sự hiểu biết của chính bạn, từ đó tăng cường sự hiểu biết cho những người xung quanh.

Để AI viết thay bạn cũng giống như bỏ tiền thuê người khác tập gym thay mình vậy.

-- [《Đừng để AI viết thay bạn》](https://alexhwoods.com/dont-let-ai-write-for-you/)

4、

Công việc của lập trình viên không phải là lập trình, mà là quản lý sự phức tạp của phần mềm thông qua việc trừu tượng hóa. Nếu bạn làm được điều đó thì việc lập trình sẽ rất dễ dàng.

-- [《Công việc của bạn không phải là lập trình》](https://codeandcake.dev/posts/2025-12-12-your-job-isnt-programming)

## Nhìn lại các năm trước

[Sản xuất đang trở thành "nền kinh tế gig"](https://www.ruanyifeng.com/blog/2025/04/weekly-issue-344.html)（#344）

[Cảm nghĩ về trận hải chiến Nhai Môn](https://www.ruanyifeng.com/blog/2024/03/weekly-issue-294.html)（#294）

[Big Data đã chết](https://www.ruanyifeng.com/blog/2023/03/weekly-issue-244.html)（#244）

[Người bi quan đúng, người lạc quan thành công](https://www.ruanyifeng.com/blog/2022/02/weekly-issue-194.html)（#194）

(Hết)
