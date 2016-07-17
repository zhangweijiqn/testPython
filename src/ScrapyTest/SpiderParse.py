__author__ = 'zhangwj'
# -*- coding: utf-8 -*-
from scrapy import Selector
st = """<!doctype html>
<html>
<head>
    <meta charset="gb2312">

<title>趾间神经痛介绍_症状_治疗_护理_饮食_疾病查询_39疾病百科</title>
<meta name="keywords" content="趾间神经痛介绍_症状_治疗_护理_饮食_疾病查询_39疾病百科">
<meta name="description" content="39健康网疾病百科为您详细介绍趾间神经痛,趾间神经痛症状,趾间神经痛治疗方法,趾间神经痛吃什么好。趾间神经痛症状：足部肿胀压痛...">

    <meta http-equiv="Cache-Control" content="no-siteapp" />
    <meta http-equiv="Cache-Control" content="no-transform" />
    <link rel="alternate" media="only screen and (max-width: 640px)" href="http://wapjbk.39.net/zjsjt/jbzs/">
    <meta name="mobile-agent" content="format=html5;url=http://wapjbk.39.net/zjsjt/jbzs/" />
    <link rel="canonical" href="http://jbk.39.net/zjsjt/jbzs/" />

    <link href="http://image.39.net/jbk/new2013/css/base2014.css" type="text/css" rel="stylesheet">
    <link href="http://image.39.net/jbk/mxb/css/chronic.css" type="text/css" rel="stylesheet">
    <script type="text/javascript" src="http://image.39.net/jquery/jquery-1.7.2.min.js"></script>
    <!--[if lt IE 9]><script src="http://image.39.net/jbk/new2013/js/html5_shiv.js" type="text/javascript"></script><![endif]-->
    <base target="_blank">

    <!--百度广告统计代码 20150325-->
<script src="http://image.39.net/gy/Head_Tools_For_jbk.js" type="text/javascript"></script>
<meta name="applicable-device" content="pc">
</head>

<body>
    <!--头部：顶部导航/关键字广告/通栏广告 logo/search 导航-->
    <header>
        <!--顶部导航-->
        <!--==================================================art_topnav 2014-->
<link href="http://image.39.net/jbk/new2013/css/jbk_topnav_2014.css" type="text/css" rel="stylesheet">
<script src="/js/topNav.js"></script>
	<div class="art_topnav_channel" id="art_topnav">
		<div class="art_wrap">
			<div class="art_navtext">
				<span class="home"><a href="http://www.39.net/" title="39健康网首页" target="_blank">39健康网首页</a></span>
				<span><a href="http://ask.39.net/" title="39问医生" target="_blank">39问医生</a></span>
				<span><a href="http://myzx.39.net/" title="名医在线" target="_blank">名医在线</a></span>
				<span><a href="http://yyk.39.net/" title="就医助手" target="_blank">就医助手</a></span>
				<span><a href="http://ypk.39.net/" title="药品通" target="_blank">药品通</a></span>
				<span><a href="http://jbk.39.net/" title="疾病百科" target="_blank">疾病百科</a></span>
				<span><a href="http://news.39.net/" title="新闻" target="_blank">新闻</a></span>
				<span><a href="http://zl.39.net/" title="诊疗" target="_blank">诊疗</a></span>
				<span><a href="http://drug.39.net/" title="药品" target="_blank">药品</a></span>
				<span class="top-qcode"><a href="http://m.39.net/jyzs/" target="_blank" title="手机挂号">手机挂号</a><em><i>30秒挂号、免费问医生<br>对症用药很重要</i><img src="http://image.39.net/daoyi/images/doc/yyk_qcode.jpg"><i>扫描下载<br>39就医助手APP</i></em></span>
			</div>
                        <script>$('.top-qcode').mouseover(function(){$(this).find('em').show();}).mouseleave(function(){$(this).find('em').hide();});</script>
			<div class="art_navlogin" id="NavLoginDiv" style="display: block;">
				<span class="n_login sbtn" id="top_loginbox">
                    <cite rel ="nofollow">登录</cite>

					<div class="n_login_box">
						<div id="drop_login" style="display:none;">
							<div class="n_login_con png">
								<form target="_self" onsubmit="return false;">
								<ul>
									<li><input type="text" name="NavUserName" id="NavUserName" class="login-input formtexts" value="用户"></li>
									<li>
										<input type="password" name="NavPassword" id="NavPassword" class="login-input" style="display:none;">
										<input type="text" name="NavPassword2" id="NavPassword2" class="login-input" value="密码">
									</li>
									<li><input type="submit" name="loginbtn" class="formbtns" onclick="NavLogin(AppID);" value=""><a href="http://my.39.net/find_password.aspx" class="wjmm">忘记密码</a></li>
								</ul>
								</form>
							</div>
							<div class="n_login_bot png"></div>
						</div>
					</div>

				</span>
				<span class="n_reg"><a href="http://my.39.net/passport/reg.aspx?ref=http://jbk.39.net" rel="nofollow">注册</a></span>

			</div>
			<div class="art_navlogin" id="NavLoginUserDiv" style="display: none;">
                <span id="NavMessageSpanBox" class="n_message sbtn"></span>
                <script type="text/javascript" src="http://my.39.net/js/myMsg.js"></script>
                <span class="n_userinfo" id="userinfo_box">
					<em><a id="NavNickName" name="NavNickName" href="http://my.39.net" target="_blank">jamkywong</a></em>
					<span class="UIbox">
						<span class="ulist png">
							<ul>
								<li><a id="NavMyAsk" name="NavMyAsk" href="http://my.39.net/UserCenter/default.aspx?menu=myquestions" target="_blank">我的提问</a></li>
								<li><a id="NavMyHome" name="NavMyHome" href="http://my.39.net" target="_blank">个人管理</a></li>
								<li class="nobline"><a href="javascript:void(0);" onclick="NavLogout(AppID);return false;">退出</a></li>
							</ul>
						</span>
						<i class="png"></i>
					</span>
				</span>
			</div>
			<script type="text/javascript">
				var AppID = 1;
			</script>
			<script type="text/javascript" src="http://my.39.net/js/NavLogin.js"></script>

		</div>

	</div>
	<!--==================================================art_topnav 2014 end -->

        <!--关键字广告/通栏广告-->
        <section class="top_ad wrap">
            <div class="top_ad_key">
                <script src="http://www.39.net/gy/topkey_jbk.js"></script>
            </div>
            <div class="top_ad_banner">
                <!--通栏广告-->
                <!-- 4851：jbk神经内科_通栏 类型：固定广告位 尺寸：1000x90 -->
<script type="text/javascript">//<![CDATA[
ac_as_id = 4851;
ac_format = 0;
ac_mode = 1;
ac_group_id = 1;
ac_server_base_url = "d.39.net/";
//]]></script>
<script type="text/javascript" src="http://image.39.net/creative/k.js"></script>
            </div>
        </section>
        <!--logo/search-->
        <link href="/Css/jquery.autocomplete.css" type="text/css" rel="stylesheet">
<script src="http://jbk.39.net/Scripts/jquery.autocomplete.js" type="text/javascript" charset="gb2312"></script>
<script src="/js/topSearch.js"></script>
  <section class="header wrap clearfix">
        <!--大logo-->
    	<a class="logo" href="http://jbk.39.net/" title="39疾病百科"><img src="http://image.39.net/jbk/new2013/img/logo.gif" alt="39疾病百科"></a>
        <span class="logo_w">收录<b id="allcount">14502</b>种疾病、症状</span>
        <!--搜索-->
		<div class="search">
        	<div class="searchTab" id="searchTab"><span class="now">疾病</span><span>检查</span><span>手术</span></div>
            <form class="searchForm clearfix" action="">
				<input id="txtSearch1" type="text" class="searchText" value="请输入疾病、症状名" onClick="if(this.value==translateTip($('#searchTab span.now').text())){this.value=''};this.style.color='#666'"  onBlur="if(this.value==''){this.value=translateTip($('#searchTab span.now').text())};this.style.color='#AAA'">
				<input id="btnSearch1" type="button" class="searchSub" value="" title="搜索">
                <a class="ask" href="javascript:void(0);" id="btnAsk"></a>
            </form>
            <div class="searchHot"><a href="http://jbk.39.net/tnb/" title="糖尿病">糖尿病</a>
                <a href="http://jbk.39.net/rxzs/" title="乳腺增生">乳腺增生</a>
                <a href="http://jbk.39.net/gxb/" title="冠心病">冠心病</a>
                <a href="http://jbk.39.net/xc/" title="哮喘">哮喘</a>
                <a href="http://jbk.39.net/gxy/" title="高血压">高血压</a>
                <a href="http://jbk.39.net/szkb/" title="手足口病">手足口病</a>
                <a href="http://jbk.39.net/gjml/" title="宫颈糜烂">宫颈糜烂</a>
            </div>

        </div>


</section>
        <!--导航-->
            <nav class="nav">
        <ul class="wrap clearfix">
            <li><a href="http://jbk.39.net/" target="_self">首页</a></li>
            <li class="now"><a href="http://jbk.39.net/bw">疾病症状</a></li>
            <li><a href="/jiancha">检查项目</a></li>
            <li><a href="/shoushu">手术项目</a></li>
            <li><a href="/zicha">症状自查</a></li>
        </ul>
        <div class="share"><span>官方微博：</span><a class="sina" href="http://weibo.com/39jbk">新浪</a></div>
    </nav>
    </header>
<!--头部 end-->

<!--内容-->
<section class="chronic wrap">
    <div class="subnav clearfix">
    <span class="sublink"><i>您现在的位置：</i><a href="http://jbk.39.net" target="_self" rel="index">疾病百科</a>&nbsp;&gt;&nbsp;<a
        href="http://jbk.39.net/bw">疾病症状</a>&nbsp;&gt;&nbsp;<b>趾间神经痛</b></span>
</div>

    <div class="spreadhead">
        <div class="ad_500">
            <!-- 4854：jbk神经内科_顶边嵌入 类型：固定广告位 尺寸：500x40 -->
<script type="text/javascript">//<![CDATA[
ac_as_id = 4854;
ac_format = 0;
ac_mode = 1;
ac_group_id = 1;
ac_server_base_url = "d.39.net/";
//]]></script>
<script type="text/javascript" src="http://image.39.net/creative/k.js"></script>
        </div>
        <div class="tit clearfix">
            <a href="http://jbk.39.net/zjsjt/"><h1>趾间神经痛</h1></a>
        </div>
        <!--疾病中栏导航-->




<div class="spreadhead-box">
    <ul class="clearfix">
        <li class="index "><a href="http://jbk.39.net/zjsjt/" title="趾间神经痛疾病首页">疾病首页</a></li>
        <li class="now"><a class=" icon1" href="http://jbk.39.net/zjsjt/jbzs/" title="趾间神经痛疾病知识">疾病知识</a></li>
            <li class=""><a class="icon2" href="http://jbk.39.net/zjsjt/zjzx/" title="趾间神经痛专家咨询">专家咨询</a></li>
        <li class=""><a class="icon3" href="http://jbk.39.net/zjsjt/yy/" title="趾间神经痛医院医生">医院医生</a></li>
                    <li class=""><a class="icon5" href="http://jbk.39.net/zjsjt/all/art/1.shtml" title="趾间神经痛文章解读">文章解读</a></li>
    </ul>
</div>
        <!--疾病中栏导航 end-->
    </div>
    <div class="content clearfix">
    	<div class="fl730 mr20">
            <div class="chi-know">
            	<dl class="intro">
                	<dt>趾间神经痛简介</dt>
                    <dd>　　神经痛或良性神经瘤可发生在任何趾间神经，趾间神经行走于趾骨之下和跖骨之间，越过跖球，走向远端，支配足趾。第三足底趾间神经由内，外足底神经的分支组成，通常在这里形成神经瘤(Morton神经瘤)。单侧神经瘤比双侧更常见，女性比男性更多。</dd>
                </dl>
                <dl class="info">
                	<dt>趾间神经痛基本知识</dt>
                    <dd><i>是否属于医保：</i><a href="http://jbk.39.net/help/" target="_blank" title="什么是医保疾病?">非医保疾病</a></dd>

                    <dd><i>发病部位：</i>
                                        <a href='/bw/shoubu/'>手部</a>
                                        <a href='/bw/zubu/'>足部</a>

                    </dd>
                    <dd><i>传染性：</i>无传染性</dd>
                    <dd><i>发人群：多</i>女性比男性更多 </dd>
                    <dd><i>相关症状：</i>
                                <a class="blue" href='http://jbk.39.net/zhengzhuang/zbzzyt/' title="足部肿胀压痛">足部肿胀压痛</a>
                                <a class="blue" href='http://jbk.39.net/zhengzhuang/zdszg/' title="足底烧灼感">足底烧灼感</a>
                                <a class="blue" href='http://jbk.39.net/zhengzhuang/sjt/' title="神经痛">神经痛</a>
                                <a class="blue" href='http://jbk.39.net/zhengzhuang/zzsqszbtt/' title="足趾伸屈时足部疼痛">足趾伸屈时足部疼痛</a>
                            <a class="more" href="http://jbk.39.net/zjsjt/zztz/">[详细]</a>

                    </dd>
                    <dd><i>并发疾病：</i>
                                    <a class="blue" href='http://jbk.39.net/zxsjt/' title="灼性神经痛">灼性神经痛</a>
                            <a class="more" href="http://jbk.39.net/zjsjt/bfbz/">[详细]</a>

                    </dd>

                </dl>
                <dl class="info">
                	<dt>趾间神经痛诊疗知识</dt>
                    <dd><i>就诊科室：</i>
                                        <a href='/bw/neike/'>内科</a>
                    </dd>
                    <dd><i>治疗费用：</i>
不同医院收费标准不一致，市三甲医院约（3000—— 6000元）                    </dd>
                    <dd><i>治愈率：</i>50%</dd>
                    <dd><i>治疗方法：</i>
                        <a class="blue" href="http://jbk.39.net/zjsjt/yyzl/">保守治疗、手术治疗</a><a class="more" href="http://jbk.39.net/zjsjt/yyzl/">[详细]</a>
</dd>
                    <dd><i>相关检查：</i>
                                   <a class="blue" href='http://jbk.39.net/jiancha/ctjc/' title="CT检查">CT检查</a>
                                   <a class="blue" href='http://jbk.39.net/jiancha/szdghgjpp/' title="四肢的骨和关节平片">四肢的骨和关节平片</a>
                                   <a class="blue" href='http://jbk.39.net/jiancha/ggcz/' title="骨骼触诊">骨骼触诊</a>
                            <a class="more" href="http://jbk.39.net/zjsjt/jcjb/">[详细]</a>

                    </dd>


                    <dd><i>常用药品：</i>
                        >><a href="http://jbk.39.net/zjsjt/yyzl/">应该如何用药？用什么药？</a>
        <!--推荐药品广告End-->
                        <a class="more" href="http://jbk.39.net/zjsjt/yyzl/">[详细]</a>
                    </dd>

                </dl>
                <dl class="info">
                    <dt>趾间神经痛去医院必看</dt>
                    <dd>
                        <i>最佳就诊时间：</i>
                            暂无相关资料
                    </dd>
                    <dd>
                        <i>就诊时长：</i>
                            暂无相关资料
                    </dd>
                    <dd>
                        <i>复诊频率/诊疗周期：</i>
                            暂无相关资料
                    </dd>
                    <dd>
                        <i>就诊前准备：</i>
                            暂无相关资料
                    </dd>
                    <dd>
                        <div style="text-align:right;"><a class="more" href="http://jbk.39.net/zjsjt/jzzn/">了解更多就诊知识&gt;&gt;</a></div>
                    </dd>
                </dl>
                <dl class="info">
                    <dt>趾间神经痛相关阅读</dt>
                    <dd style="text-indent:0em">
                        <a href="http://jbk.39.net/zjsjt/blby/" style="margin-right:40px;">趾间神经痛是怎么引起的</a><a href="/zicha" style="margin-right:40px;">趾间神经痛自测</a><a href="http://jbk.39.net/zjsjt/yyzl/" style="margin-right:40px;">如何治疗趾间神经痛</a><a href="http://jbk.39.net/zjsjt/ysbj/">趾间神经痛吃什么好</a>
                    </dd>
                </dl>
            </div>
            <!-- 5083：pc-jbk底部位置 类型：固定广告位 尺寸：728x90 -->
<script type="text/javascript">//<![CDATA[
ac_as_id = 5083;
ac_format = 0;
ac_mode = 1;
ac_group_id = 1;
ac_server_base_url = "d.39.net/";
//]]></script>
<script type="text/javascript" src="http://image.39.net/creative/k.js"></script>
        </div>
        <div class="fl250">
            <!--百度临时广告-->
            <!-- 5326：疾病百科-疾病页右上图标 类型：固定广告位 尺寸：250x250 -->

<script type="text/javascript">//<![CDATA[

ac_as_id = 5326;

ac_format = 0;

ac_mode = 1;

ac_group_id = 1;

ac_server_base_url = "d.39.net/";

//]]></script>

<script type="text/javascript" src="http://image.39.net/creative/k.js"></script>
            <!--专家在线咨询-->
            <!-- 4853：jbk神经内科_专家在线咨询 类型：固定广告位 尺寸：250x490 -->
<script type="text/javascript">//<![CDATA[
ac_as_id = 4853;
ac_format = 0;
ac_mode = 1;
ac_group_id = 1;
ac_server_base_url = "d.39.net/";
//]]></script>
<script type="text/javascript" src="http://image.39.net/creative/k.js"></script>
            <!--百度临时广告-->
            <!-- 5327：疾病百科-疾病页右侧中部图标 类型：固定广告位 尺寸：250x250 -->

<script type="text/javascript">//<![CDATA[

ac_as_id = 5327;

ac_format = 0;

ac_mode = 1;

ac_group_id = 1;

ac_server_base_url = "d.39.net/";

//]]></script>

<script type="text/javascript" src="http://image.39.net/creative/k.js"></script>
            <!--推荐医院-->


        	<div class="chr-rbox">


        <div class="item">
            <div class="tit clearfix">
                <h3>慢性病治疗方法</h3>
                <a href="http://jbk.39.net/zq/manxingbing/hl" class="tit-more">更多&gt;&gt;</a>

            </div>
            <ul class="list">

                        <li><a href="http://disease.39.net/sj/083/30/308217.html" title="臂丛神经痛针灸治疗">臂丛神经痛针灸治疗</a></li>
                        <li><a href="http://woman.39.net/a/201086/1431510.html" title="中看不中吃的山珍海味">中看不中吃的山珍海味</a></li>
                        <li><a href="http://mouth.39.net/083/6/266839.html" title="三叉神经痛的治疗及效用">三叉神经痛的治疗及效用</a></li>
                        <li><a href="http://disease.39.net/sj/083/29/307704.html" title="臂丛神经痛中医辩病治疗">臂丛神经痛中医辩病治疗</a></li>
                        <li><a href="http://drug.39.net/a/141211/4535280.html" title="老人如何使用镇痛药更安全">老人如何使用镇痛药更安全</a></li>
            </ul>
        </div>








                    <div class="item">
    <div class="tit clearfix">
        <h3 title="趾间神经痛相关疾病">相关疾病</h3>
    </div>
    <ul class="list3 clearfix">
            <li><a href="http://jbk.39.net/dx/">癫痫</a></li>
            <li><a href="http://jbk.39.net/zgsjt/">坐骨神经痛</a></li>
            <li><a href="http://jbk.39.net/sjsr/">神经衰弱</a></li>
            <li><a href="http://jbk.39.net/ptt/">偏头痛</a></li>
            <li><a href="http://jbk.39.net/zwsjgnwl/">植物神经功能紊乱</a></li>
            <li><a href="http://jbk.39.net/nxs/">脑血栓</a></li>
            <li><a href="http://jbk.39.net/xgsjxsz/">血管神经性水肿</a></li>
            <li><a href="http://jbk.39.net/jgsjxjzb/">交感神经型颈椎病</a></li>
            <li><a href="http://jbk.39.net/jxjsy/">急性脊髓炎</a></li>
            <li><a href="http://jbk.39.net/jzxtt/">紧张性头痛</a></li>
            <li><a href="http://jbk.39.net/jwscsyhz/">肌萎缩侧索硬化症</a></li>
            <li><a href="http://jbk.39.net/jskdz/">脊髓空洞症</a></li>
    </ul>
    </div>




                <!--相关标签-->
                <div class="item">
    <div class="tit clearfix">
        <h3 title="趾间神经痛相关标签">相关标签</h3>
    </div>
    <ul class="tag-rel clearfix">
        <li><a href="http://jbk.39.net/zjsjt/">趾间神经痛知识概述</a></li>
        <li><a href="http://jbk.39.net/zjsjt/jbzs/">趾间神经痛是什么</a></li>
        <li><a href="http://jbk.39.net/zjsjt/zztz/">趾间神经痛的症状表现</a></li>
        <li><a href="http://jbk.39.net/zjsjt/blby/">趾间神经痛是怎么引起的</a></li>
        <li><a href="http://jbk.39.net/zjsjt/yfhl/">如何预防趾间神经痛</a></li>
        <li><a href="http://jbk.39.net/zjsjt/jcjb/">趾间神经痛怎么检查</a></li>
        <li><a href="http://jbk.39.net/zjsjt/jb/">趾间神经痛诊断与治疗</a></li>
        <li><a href="http://jbk.39.net/zjsjt/yyzl/">趾间神经痛怎么治疗</a></li>
        <li><a href="http://jbk.39.net/zjsjt/hl/">趾间神经痛怎么调理</a></li>
        <li><a href="http://jbk.39.net/zjsjt/ysbj/">有趾间神经痛吃什么好</a></li>
        <li><a href="http://jbk.39.net/zjsjt/bfbz/">趾间神经痛并发症</a></li>

            <li><a href="http://jbk.39.net/zjsjt/zjzx/">趾间神经痛专家咨询</a></li>

        <li><a href="http://jbk.39.net/zjsjt/yy/">趾间神经痛推荐医院</a></li>
        <li><a href="http://jbk.39.net/zjsjt/ys/">趾间神经痛推荐医生</a></li>
        <li><a href="/zjsjt/all/art/1.shtml">趾间神经痛相关知识</a></li>
    </ul>
</div>
                <!--相关词条-->

            </div>
        </div>
    </div>
</section>
<!--内容 end-->
    <!--左浮标广告-->
    <!-- 2895：jbk神经内科_浮标 类型：浮层广告位 尺寸：- -->
<script type="text/javascript">//<![CDATA[
ac_as_id = 2895;
ac_format = 0;
ac_mode = 1;
ac_group_id = 1;
ac_server_base_url = "d.39.net/";
//]]></script>
<script type="text/javascript" src="http://image.39.net/creative/k.js"></script>
<!--左侧滚动导航-->



<div class="leftNav">
    <ul>
            <li>
                    <b>疾病简介</b>
            </li>
                <li>
                <a href="http://jbk.39.net/zjsjt/zztz/" target="_self">典型症状</a>
        </li>
                <li>
                <a href="http://jbk.39.net/zjsjt/blby/" target="_self">发病原因</a>
        </li>
                <li>
                <a href="http://jbk.39.net/zjsjt/yfhl/" target="_self">预防</a>
        </li>
                <li>
                <a href="http://jbk.39.net/zjsjt/jcjb/" target="_self">临床检查</a>
        </li>
                <li>
                <a href="http://jbk.39.net/zjsjt/jb/" target="_self">鉴别</a>
        </li>
                <li>
                <a href="http://jbk.39.net/zjsjt/yyzl/" target="_self">治疗方法</a>
        </li>
                <li>
                <a href="http://jbk.39.net/zjsjt/hl/" target="_self">护理</a>
        </li>
                <li>
                <a href="http://jbk.39.net/zjsjt/ysbj/" target="_self">饮食保健</a>
        </li>
                    <li>
                    <a href="http://jbk.39.net/zjsjt/bfbz/" target="_self">并发症</a>
            </li>
        <li>

                <a href="/zicha">疾病自测</a>
        </li>
    </ul>
</div>
<!--左侧滚动导航 end-->

<!--底部相关-->
    <script type="text/javascript">
        bfdtitle = "趾间神经痛";
        bfdid = "355723";
        bfdurl = "http://jbk.39.net/zjsjt/";
        bfdcategory = [["疾病百科", "http://jbk.39.net/"], ["疾病症状", "http://jbk.39.net/bw"], ["趾间神经痛", "http://jbk.39.net/zjsjt/"]];
        bfdpagetype = "jbzs_detail";
    </script>
<!--底部-->
<footer>
    <section class="foot_prompt">
        <div class="copyrightbox"><p>39健康网版权所有，未经许可不得转载！（软件版权2008SR31117，内容版权19-2008-L-0118。）</p></div>
    </section>
    <section class="foot_copyright">
        <div class="bottominfo wrap" id="bottominfo">
            <a href="http://corp.39.net/info/about.html" rel="nofollow" hidefocus="true">网站简介</a> |
            <a href="http://jbk.39.net/map" hidefocus="true">网站地图</a> |
            <a href="http://daohang.39.net/" rel="nofollow" hidefocus="true">友情链接</a> |
            <a href="http://news.39.net/mtbd/" rel="nofollow" hidefocus="true">媒体报道</a> |
            <a href="http://links.39.net/nylj" rel="nofollow" hidefocus="true">合作伙伴</a> |
            <a href="http://job.39.net/" rel="nofollow" hidefocus="true">人才招聘</a> |
            <a href="http://corp.39.net/adcenter/" rel="nofollow" hidefocus="true">网络营销中心</a> |
            <a href="http://corp.39.net/info/contact.html" rel="nofollow" hidefocus="true">联系方式</a> |
            <a href="http://jbk.39.net/" name="homepage" target="_self" rel="nofollow" hidefocus="true">电脑版</a> |
            <a href="http://wapjbk.39.net/" target="_self" rel="nofollow" hidefocus="true">手机版</a><br>
            Copyright &copy 2000-
            <script type="text/javascript"> var myDate = new Date(); document.write(myDate.getFullYear());</script>　39.net All Rights Reserved.　39健康网 <a href="http://corp.39.net/info/disclaimer.html" rel="nofollow" hidefocus="true">版权所有</a>
        </div>
    </section>
    <script type="text/javascript" src="http://image.39.net/js/fun_index.js?v=20121016051607"></script>
</footer>
<!--底部 end-->
<!-- 右侧浮动-->
<div class="floatSide">
    <a class="code" title="二维码" style="display: block;" rel="nofollow"></a>
    <dl class="coder" title="二维码" style="display: none;">
        <dt><img src="http://image.39.net/jbk/new2013/img/pic/code.jpg"></dt>
        <dd>微信查询更惊喜<br />马上扫描关注</dd>
    </dl>
    <a class="advice" title="反馈意见" id="advice" href="javascript:void(0)" rel="nofollow"></a>
    <a class="totop" title="回到顶部" onclick="window.scrollTo(0,0);return false" rel="nofollow"></a>
</div>

<script src="/js/bfd.js" type="text/javascript"></script>
<!-- 右侧浮动 end-->
<div><object id="ClCache" click="sendMsg" host="" width="0" height="0"></object></div>
<script type="text/javascript" src="http://image.39.net/jbk/new2013/js/jbk_common_2014.js"></script>
<script src="http://img.39.net/js/db/wt.js" type="text/javascript"></script>
<script src="http://image.39.net/tools/djan.js" type="text/javascript"></script>
<script type="text/javascript">
var url = window.location.href;
if (url.indexOf("hmrl") >= 0){
$("#BAIDU_DSPUI_FLOWBAR").css('display','none');
$("#BAIDU_DSPUI_FLOWBAR").hide();
$("#BAIDU_SSP__wrapper_u2209818_0").hide();
$("#BAIDU_SSP__wrapper_u2209818_0").css('display','none');
$("#BAIDU_SSP__wrapper_u1548960_0").hide();
$("#BAIDU_SSP__wrapper_u1548960_0").css('display','none');
}
</script>
<!--底部相关end-->
<script type="text/javascript" src="http://image.39.net/jbk/new2013/js/jbk_common_2014.js"></script>
<script type="text/javascript" src="http://image.39.net/jbk/mxb/js/chronic.js"></script>

</body>
</html>
<!--5秒-->
"""

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

_x_query = {		#元素提取
                    'name':'//h1/text()',
                    'introduct':'//dl[@class="intro"]/dd/text()',
                    'info':'//div[@class="chi-know"]/dl[@class="info"]/dd',
                    'commom_symptom':'//div[@class="chi-know chi-int"]/dl[@class="links"]',
                    'common_complicated':'//div[@class="chi-know chi-int"]/dl[@class="links"]'
                    }
def getKey(lst=[],sep="|"):
    new_lst=[]
    for l in lst:
        tmp = str(l).strip()
        if(tmp!=''):
            pos = tmp.find("：")
            if(pos>0):
                new_lst.append(tmp[0:len(tmp)-3])
            else:
                new_lst.append(tmp)
    return sep.join(new_lst).strip()

def getValue(lst=[],sep="|"):
    new_lst=[]
    for l in lst:
        tmp = str(l).strip()
        if(tmp!=''):
            if tmp.find("：")<0 and tmp.find("详细")<0:
                new_lst.append(tmp)
    return sep.join(new_lst).strip()

sel = Selector(text=st,type="html")

tmp = {}

index=1
for dd in sel.xpath(_x_query['info']):
    k = getKey(dd.xpath("./i//text()").extract())
    # k = ','.join(dd.xpath("./i//text()").extract())
    print "k=",k
    v = getValue(dd.xpath("./a//text()").extract())
    if ''==v:
        v = getValue(dd.xpath(".//text()").extract())
    print "v=",v
    if ''!=k:
        tmp[str(k)]=str(v)
    index+=1
    if index>17:break    #只抓取info下前17个dd元素的内容

print tmp

import codecs
import json
file1 = codecs.open('test.txt', 'wb')
line = json.dumps(dict(tmp),ensure_ascii=False)+"\n"
print "line=",line
file1.write(line)

