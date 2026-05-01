# Đầu độc axios và những màn kịch kiểu Hollywood

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040203.webp)

Đây là khuôn viên trụ sở mới của Tencent, thường được gọi là "Đảo Cánh Cụt", dự kiến sẽ đi vào hoạt động trong năm nay. Nơi đây không chỉ có các tòa nhà văn phòng hiện đại mà còn bao gồm nhiều khu căn hộ cho nhân viên. ([via](https://www.nfnews.com/content/0oXLNmjJo9.html))

## Đầu độc axios và những màn kịch kiểu Hollywood

Tuần trước, thư viện phần mềm nổi tiếng axios vừa bị [đầu độc](https://cloud.tencent.com/announce/detail/2249). Hacker đã chiếm được token phát hành và tung ra một phiên bản mới có cài cắm mã độc.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040703.webp)

Việc đầu độc phần mềm thì không mới, nhưng điều khiến tôi kinh ngạc là cách mà token bị rò rỉ. Đó thực sự là một kịch bản hoàn hảo đến mức nghẹt thở, hệt như trong các bộ phim Hollywood.

Với một thư viện có tới gần 100 triệu lượt tải mỗi tuần như axios, sức ảnh hưởng của vụ tấn công này là vô cùng khủng khiếp.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040704.webp)

Mã độc lần này cực kỳ nguy hiểm. Theo [hướng dẫn xử lý từ phía dự án](https://github.com/axios/axios/issues/10636#issue-4195231282), nếu chẳng may dính đòn, **bạn buộc phải hủy bỏ toàn bộ key, token và chứng chỉ trên máy**. Con mã độc này sẽ quét sạch mọi ngóc ngách trong thư mục để thu thập thông tin nhạy cảm và gửi về server của hacker.

Bạn nên biết rằng với những dự án tầm cỡ như axios, mỗi quy trình bảo mật đều cực kỳ nghiêm ngặt và mã nguồn được kiểm soát chặt chẽ. **Cuộc tấn công này hoàn toàn là một nỗ lực thao túng tâm lý (social engineering) được dàn dựng vô cùng công phu** để xuyên thủng mọi lớp phòng vệ.

Mục tiêu nhắm tới là Jason Saayman, người duy trì dự án chính. [Anh kể lại](https://github.com/axios/axios/issues/10636#issuecomment-4180237789) hành trình sập bẫy của mình như thế này:

> Hacker đã thiết kế một kịch bản "đo ni đóng giày" cho tôi:
> 
> 1. Họ giả danh nhà sáng lập của một công ty thật để liên hệ với tôi. Từ diện mạo cho đến thông tin về công ty đều được sao chép y như đúc.
> 2. Sau đó, họ mời tôi vào một nhóm Slack "xịn". Nhóm này sử dụng bộ nhận diện thương hiệu của công ty đó, tên nhóm cũng rất đáng tin. Nhóm Slack được dàn dựng rất chuyên nghiệp, có cả các kênh thảo luận về những bài đăng trên LinkedIn. Họ thậm chí còn tạo ra hàng loạt tài khoản ảo đóng vai nhân viên công ty và các lập trình viên mã nguồn mở nổi tiếng khác.
> 3. Họ sắp xếp một buổi họp online qua Microsoft Teams để bàn công việc.
> 4. Trong lúc họp, họ bảo hệ thống của tôi đang dùng bản cũ, khiến Teams không tương thích. Tôi tin lời và cài đặt bộ "linh kiện" họ gửi qua, nhưng hóa ra đó lại là mã độc RAT (Remote Access Trojan).
> 5. Mọi thứ được dàn dựng chuyên nghiệp và logic đến mức tôi không mảy may nghi ngờ.

Có thể thấy, đây là một cuộc tấn công có kịch bản chi tiết, được chuẩn bị và tập dượt kỹ lưỡng để nhắm thẳng vào một cá nhân cụ thể.

Kẻ lừa đảo cực kỳ kiên nhẫn và đã đầu tư rất lớn cho giai đoạn chuẩn bị. Đầu tiên là giả mạo nhà sáng lập và dựng website công ty giả. Sau đó là mời vào nhóm Slack với đầy đủ tài liệu và các cuộc thảo luận như thật. Đỉnh điểm là họ còn cử cả một nhóm lừa đảo lộ diện để họp video cùng bạn trên Teams.

Khi buổi họp đang diễn ra, người chủ trì bất ngờ bảo: "Ơ, sao máy anh khác máy tôi thế nhỉ, có lẽ plugin Microsoft của anh cũ rồi, để tôi gửi bản mới nhất cho". Thấy mọi người đang chờ, Jason đã không ngần ngại chạy file cài đặt đó. Và thế là xong, token phát hành của axios đã rơi vào tay hacker chỉ trong một nốt nhạc.

Sự dàn dựng đến mức này thực sự khiến người ta phải ngả mũ.

Nó làm tôi nhớ đến một [tin tức từ Ấn Độ](https://www.wsj.com/world/fake-cops-fake-judges-the-hollywood-style-scam-poised-to-go-global-e1e339a3?st=fXpKE6&mod=1440&user_id=66c4c9305d78644b3ac5df9c) cách đây không lâu, với mức độ dàn dựng còn kinh khủng hơn nhiều, cũng hệt như phim Hollywood.

Giáng sinh năm ngoái, một bà cụ 77 tuổi ở New Delhi nhận được cuộc gọi video qua Whatsapp từ "đồn cảnh sát". Thậm chí ở góc màn hình còn có cả người phiên dịch ngôn ngữ ký hiệu.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040405.webp)

"Cảnh sát" bảo tài khoản của bà có dấu hiệu rửa tiền và yêu cầu bà phải tham gia một buổi điều trần trực tuyến tại "tòa án".

Sau này báo chí mới phanh phui hình ảnh hiện trường của cái "đồn cảnh sát" giả đó. Hãy xem nó chân thực đến mức nào.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040406.webp)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040407.webp)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040408.webp)

Ba bức ảnh đầu là đồn cảnh sát Ấn Độ, còn bức cuối là đồn cảnh sát Pakistan. Chúng nằm ngay sát vách nhau trong cùng một tòa nhà. Ngoài đời hai nước này vốn đối đầu nhau, nhưng đám lừa đảo thì vẫn sẵn sàng "hợp tác" để đi lừa khắp nơi.

Quay lại vụ án, vài ngày sau bà cụ tham gia buổi điều trần online do một "thẩm phán" chủ trì. Ông ta xem xét hồ sơ, nghe nhân chứng và hỏi cung bà cụ rất bài bản. Sau đó, ông ta yêu cầu bà phải giữ liên lạc với cảnh sát mỗi ngày để phục vụ điều tra cho đến khi sáng tỏ.

Và đây mới là phần đỉnh cao của vở kịch: Suốt 16 ngày liên tiếp, bà cụ hằng ngày đều mở camera để trò chuyện với đám cảnh sát giả này.

> Trong 16 ngày đó, bà cụ dần nảy sinh tình cảm với những "viên cảnh sát" trực ban. Bà gọi họ là con, còn họ cũng ngọt ngào gọi bà là "mẹ".
> Buổi tối, bà cùng một viên cảnh sát trẻ nhất đọc kinh thánh, và anh ta còn nhờ bà gửi cho mình những đoạn kinh mà bà thấy tâm đắc.
> "Họ giống như người thân của tôi vậy," bà cụ nhớ lại. "Họ bảo: 'Mẹ ơi, chúng con đang nỗ lực ngày đêm để sớm giải quyết xong việc này cho mẹ'".

Thật không thể tin nổi, đám lừa đảo đã kiên trì diễn kịch ròng rã 16 ngày, tâm sự thâu đêm suốt sáng với nạn nhân chỉ để lấy lòng tin. Nếu quay thành phim, có lẽ đây sẽ là một bộ phim vô cùng cảm động.

Kết quả là bà cụ đã không chút nghi ngờ, tự nguyện bán sạch các khoản đầu tư và chuyển tổng cộng 1,6 triệu USD cho "đồn cảnh sát". Đến ngày hôm sau, bà không còn liên lạc được với "những đứa con cảnh sát" nữa.

Hai câu chuyện trên cho thấy các chiêu trò lừa đảo thời nay đã tiến hóa đến mức thượng thừa. Chúng không còn là những tin nhắn rác ngớ ngẩn mà là những "kịch bản đo ni đóng giày" với tỉ lệ thành công cực cao. Với sự trợ giúp của AI, việc phân biệt thật giả có lẽ sẽ trở thành nhiệm vụ bất khả thi.

Trong phát triển web có một quy tắc: mọi yêu cầu từ phía client đều không thể tin tưởng. Có lẽ sắp tới, trong đời thực chúng ta cũng phải sống như vậy: không bao giờ tin tưởng bất kỳ người lạ nào.

## Sức mạnh tính toán vẫn chưa đủ

Ba sự kiện gần đây cho thấy tài nguyên tính toán (compute) vẫn đang cực kỳ khan hiếm.

Đầu tiên, OpenAI vừa phải [tạm dừng](https://finance.sina.cn/stock/jdts/2026-04-07/detail-inhtsezc7221412.d.html) dịch vụ tạo video Sora. Lý do chính là thiếu hụt tài nguyên để vận hành, buộc họ phải ưu tiên cho các mảng cốt lõi.

Thứ hai, Anthropic chính thức cấm việc dùng gói thuê bao tháng cho các dịch vụ bên thứ ba (như OpenClaw hay OpenCode). Lý do là chi phí tài nguyên để vận hành các dịch vụ này vượt xa số tiền người dùng trả cho gói thuê bao. Họ phải ưu tiên tài nguyên cho "gà nhà" như Claude Code.

Thứ ba, một [số liệu từ GitHub](https://martinalderson.com/posts/what-next-for-the-compute-crunch/) cho thấy lượng commit trong 3 tháng đầu năm nay tăng gấp 14 lần so với cùng kỳ năm ngoái! Sự bùng nổ của lập trình bằng AI chính là nguyên nhân. GitHub đang phải gồng mình chống đỡ dẫn đến [liên tục gặp sự cố](https://mrshu.github.io/github-statuses/).

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040810.webp)

Nhìn biểu đồ trên, tỷ lệ uptime của GitHub trong ba tháng qua chỉ đạt 89,47%, trong khi con số tiêu chuẩn phải là 99,99%.

Tất cả cho thấy các ông lớn AI vẫn đang rất thiếu phần cứng. Điều này đồng nghĩa với việc giá phần cứng sẽ còn tăng, và những dịch vụ miễn phí như GitHub có lẽ sẽ sớm bị siết chặt và thu phí toàn diện.

## Frontend có phải là công việc lặp đi lặp lại?

Một nhà phát triển đã [thẳng thắn nhận định](https://jonno.nz/posts/what-if-your-browser-built-the-ui-for-you/) rằng: bản chất của Frontend chỉ quanh quẩn việc hiển thị dữ liệu và cho phép người dùng thao tác trên đó.

Anh ta cảm thấy không cần thiết phải giải quyết đi giải quyết lại cùng một vấn đề, nên đã tạo ra một "[trình duyệt tự thích ứng](https://github.com/jonnonz1/adaptive-browser)". Hệ thống này dùng AI để tự động tạo ra giao diện người dùng dựa trên dữ liệu và mô tả chức năng từ phía backend. Liệu đây có phải là cái kết cho nghề Frontend?

## Adobe và chiêu trò sửa file hosts

Bộ công cụ Creative Cloud của Adobe chắc hẳn không còn xa lạ gì với dân thiết kế, với những Photoshop, Illustrator hay Premiere.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040404.webp)

Thế nhưng, một người dùng đã [phát hiện ra](https://www.reddit.com/r/webdev/comments/1sb6hzk/comment/oe1ap9h/) một sự thật gây sốc: bộ cài đặt của Adobe đã âm thầm sửa đổi file hosts trên máy tính của anh ta.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040403.webp)

Adobe đã chèn thêm một bản ghi DNS nội bộ vào file hosts. Tại sao một phần mềm danh tiếng lại phải làm trò này?

Hóa ra, đây là cách để họ kiểm tra xem người dùng có đang cài Creative Cloud hay không. Khi bạn truy cập website của Adobe, trang web sẽ gửi một request tới cái domain ảo đó. Vì bản ghi DNS này chỉ tồn tại trên máy cục bộ, nên nếu server nhận được request thì nghĩa là máy bạn đã cài phần mềm của họ. Một hãng phần mềm lớn mà lại dùng chiêu "đi cửa sau" với chính khách hàng trả tiền cho mình thì đúng là khó chấp nhận.

## Bài viết hay

1、[Giải mã kiến trúc Frontend của MDN](https://developer.mozilla.org/en-US/blog/mdn-front-end-deep-dive/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040801.webp)

MDN là kho tàng tài liệu khổng lồ cho dân web. Bài viết này hé lộ kiến trúc Frontend cực kỳ phức tạp đứng sau website này.

2、[Kẻ viết code và sự kết thúc của một thời đại](https://windliang.wang/2026/03/31/%E6%9D%80%E6%AD%BB%E9%82%A3%E4%B8%AA%E5%86%99%E4%BB%A3%E7%A0%81%E7%9A%84%E4%BA%BA/) (Tiếng Trung)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040813.webp)

Một lập trình viên Frontend chia sẻ về hành trình chuyển từ code tay sang lập trình bằng AI. AI đã thay đổi mọi thứ và xóa bỏ nỗi lo "về hưu tuổi 35". ([@wind-liang](https://github.com/ruanyf/weekly/issues/9545) đóng góp)

3、[Tự chế SMS Gateway từ điện thoại Android cũ](https://jonno.nz/posts/built-an-sms-gateway-with-a-20-dollar-android-phone/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040302.webp)

Hướng dẫn cách tận dụng một chiếc điện thoại Android cũ để làm cổng gửi tin nhắn SMS qua mạng.

4、[Kiểm tra Big-Endian bằng QEMU](https://www.hanshq.net/big-endian-qemu.html) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040402.webp)

Một bài hướng dẫn cơ bản về C để kiểm tra xem một kiến trúc máy tính là Big-Endian hay Little-Endian thông qua máy ảo QEMU.

5、[Tính năng importtime trong Python](https://simonwillison.net/2025/Jun/20/python-importtime-graph/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025062101.webp)

Việc import các module trong Python cũng tốn tài nguyên. Bài viết giới thiệu tính năng giúp bạn đo đạc chính xác thời gian tải của từng module.

6、[Thảm họa tàu ngầm hạt nhân Kursk năm 2000](https://rarehistoricalphotos.com/kursk-submarine-disaster-photos/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040808.webp)

Tháng 8 năm 2000, tàu ngầm hạt nhân Kursk của Nga bị nổ và chìm trong một buổi diễn tập. 118 thủy thủ đã thiệt mạng. Bài viết tái hiện lại thảm kịch này qua những hình ảnh tư liệu quý giá.

## Công cụ

1、[Google AI Edge Gallery](https://apps.apple.com/nl/app/google-ai-edge-gallery/id6749645337)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040601.webp)

Google vừa ra mắt App trên iOS cho phép chạy mô hình Gemma 4 hoàn toàn offline ngay trên điện thoại của bạn.

2、[apfel](https://apfel.franzai.com/)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040401.webp)

Công cụ giúp bạn gọi mô hình AI tích hợp sẵn trên Mac trực tiếp từ dòng lệnh.

3、[Docking](https://docking.cc/)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040701.webp)

Thêm thanh Dock phong cách macOS cho các máy chạy Linux.

4、[Tantivy](https://github.com/quickwit-oss/tantivy)

Thư viện tìm kiếm toàn văn bằng Rust, một giải pháp thay thế tiềm năng cho Apache Lucene.

5、[Open Screen](https://github.com/siddharthvaddem/openscreen)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040501.webp)

Ứng dụng quay màn hình và tạo video giới thiệu sản phẩm chuyên nghiệp, đa nền tảng.

6、[epub-tts](https://github.com/rafael1mc/epub-tts)

Công cụ mã nguồn mở giúp chuyển đổi file ebook định dạng epub thành sách nói (audiobook).

7、[NVTOP](https://github.com/Syllo/nvtop)

![](https://cdn.beekka.com/blogimg/asset/202403/bg2024031301.webp)

Công cụ dòng lệnh giúp theo dõi trạng thái GPU trên Linux, tương tự như lệnh top.

8、[dmcheck](https://github.com/PlayerYK/dmcheck)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040812.webp)

Kiểm tra trạng thái chiếm dụng tên miền của một từ khóa nhất định. ([@PlayerYK](https://github.com/ruanyf/weekly/issues/9542) đóng góp)

9、[Reze Studio](https://github.com/AmyangXYZ/reze-studio)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040901.webp)

Website mã nguồn mở hỗ trợ tinh chỉnh các đường cong chuyển động trong hoạt ảnh. ([@AmyangXYZ](https://github.com/ruanyf/weekly/issues/9555) đóng góp)

10、[gitlogue](https://github.com/unhappychoice/gitlogue)

Tái hiện lịch sử commit của kho lưu trữ Git dưới dạng hoạt ảnh ngay trong terminal.

## Tài nguyên

1、[Phật Tân (Fojin)](https://fojin.app/)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040301.webp)

Nền tảng số hóa kho tàng kinh điển Phật giáo toàn cầu. ([@xr843](https://github.com/ruanyf/weekly/issues/9507) đóng góp)

2、[Flight Viz](https://flight-viz.com/)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040811.webp)

Theo dõi các chuyến bay trên toàn thế giới theo thời gian thực dưới dạng 3D. ([@haojiang99](https://github.com/ruanyf/weekly/issues/9538) đóng góp)

3、[Dòng thời gian của GPU](https://sheets.works/data-viz/every-gpu)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040809.webp)

Nhìn lại lịch sử phát triển của card đồ họa, từ những chiếc Voodoo đầu tiên đến RTX 5090.

## Hình ảnh

1、[Cách đơn giản để xanh hóa đồi trọc](https://www.sciencealert.com/how-12-000-tonnes-of-dumped-orange-peel-produced-something-nobody-imagined)

Tại Costa Rica, người ta đã đổ 12.000 tấn vỏ cam bỏ đi lên một vùng đồi trọc để làm phân bón.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040802.webp)

Toàn bộ sườn đồi được bao phủ bởi vỏ cam và không cần thêm bất kỳ tác động nào khác.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040803.webp)

Sau 6 tháng, vỏ cam thối rữa hoàn toàn thành bùn đen, và cây cỏ bắt đầu mọc lên.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040804.webp)

16 năm sau, khi các nhà khoa học quay lại, nơi đây đã trở thành một khu rừng xanh tốt.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040805.webp)

Đây thực sự là phương pháp phủ xanh đơn giản đến mức không ai ngờ tới: chỉ cần đổ đầy vỏ cam và để chúng tự phân hủy.

2、[Cuộc thi ảnh vật lý toàn cầu 2025](https://www.quantamagazine.org/global-physics-photowalk-2025-winners-revealed-20260401/)

Các phòng thí nghiệm vật lý hạt hàng đầu thế giới đã tổ chức một cuộc thi nhiếp ảnh nhằm quảng bá vật lý học đến công chúng.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040806.webp)

Đây là phòng thí nghiệm máy dò nhiệt độ thấp tại Italy, nơi vật chất được làm lạnh đến mức gần sát độ không tuyệt đối.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040807.webp)

Còn đây là hệ thống cung cấp năng lượng cho máy gia tốc tuyến tính tại Pháp.

## Văn trích

1、[Tại sao cát lại có tính dính?](https://www.mentalfloss.com/posts/why-is-sand-sticky)

Bản thân cát không dính, nhưng nó có tính ưa nước.

![](https://cdn.beekka.com/blogimg/asset/202304/bg2023042604.webp)

Khi cát tiếp xúc với mồ hôi trên da hoặc nước biển, các phân tử nước sẽ tạo ra lực liên kết khiến cát bám chặt lấy bạn. Cách tốt nhất để rũ bỏ chúng là đợi cho da khô hẳn hoặc dùng nước rửa sạch.

## Trích dẫn

1、

Nếu bạn nghĩ tốc độ viết code là vấn đề lớn nhất của mình, thì thực ra bạn đang gặp phải những vấn đề còn lớn hơn thế nhiều.

-- Andrew Murphy

2、

Có một kiểu hưng phấn đặc thù, đó là kiểu hưng phấn của những người mới bắt đầu chạm tay vào tiền mã hóa từ năm 2017.

-- Andrew Murphy

3、

Giới trẻ ngày nay có vẻ lạnh nhạt với những giá trị truyền thống như gia đình hay lòng yêu nước. Họ coi thị trường và tiền bạc mới là thước đo chuẩn mực cho mọi thứ.

-- Trích "Hệ lụy tồi tệ của thị trường dự đoán"

4、

Tương lai của đô thị với tôi là những con phố yên bình và làn đường cho xe đạp như ở Amsterdam, chứ không phải những xa lộ 16 làn xe ở Dubai.

-- Một độc giả Hacker News

5、

Các trường đại học ép nghiên cứu sinh phải ra bài báo khoa học. Đôi khi họ chẳng quan tâm bạn viết gì, bài báo chỉ là công cụ để chứng minh kinh phí nghiên cứu là hợp lý. Sinh viên suy cho cùng cũng chỉ là một dạng tư liệu sản xuất.

-- Trích "Máy móc không có lỗi, lỗi ở chính chúng ta"

(Hết)
