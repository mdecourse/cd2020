import 'dart:html';
import 'dart:convert';

  InputElement studListUrl = querySelector("#studListUrl");
  String studUrl;
  InputElement number = querySelector("#number");
  int num;
  // 將 Label 改為 Textarea, 避免產生過程結果嵌入所在頁面
  TextAreaElement output = querySelector("#output");
 
main() {
  querySelector("#submit").onClick.listen((e) => randomSelect());
}


//String grpList = 'https://mde.tw/cd2020/downloads/2a_group_list.txt';
//int num = 2;

randomSelect() {

  output.innerHtml = "";
 
  if (studListUrl.value != "") {
    studUrl = studListUrl.value;
  } else {
    studUrl = 'https://mde.tw/cd2020/downloads/2a_group_list.txt';
  }
  
  if (number.value != ""){
    num = number.value;
  } else {
      num = 2;
  }
  
  HttpRequest.getString(studUrl)
    // assign response as variable resp
    .then((String resp){
      // remove all "'" to allow jsonDecode string into list
      final replaced = resp.replaceAll("'", '');
      List studList = jsonDecode(replaced);
      for (int i=0; i<studList.length; i++)
      {
        // shuffle studList element
        studList[i].shuffle();
        // draw num of member from each group
        //print("-"*20);
	output
        for (int j=0; j<num; j++)
        {
          print("group ${i+1}:" + studList[i][j].toString());
        }
      }
    });
}