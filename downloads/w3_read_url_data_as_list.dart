import 'dart:html';
import 'dart:convert';


String grpList = 'https://mde.tw/cd2020/downloads/2a_group_list.txt';
int num = 2;

void main() {
  
  HttpRequest.getString(grpList)
    // print response directory
    //.then(print);
    // assign response as variable resp
    .then((String resp){
      // get group List from URL
      //print(resp);
      // remove all "'" to allow jsonDecode string into list
      final replaced = resp.replaceAll("'", '');
      //print(replaced);
      // check if jsonDecode works
      //print(jsonDecode(replaced)[0]);
      List studList = jsonDecode(replaced);
      for (int i=0; i<studList.length; i++)
      {
        // shuffle studList element
        studList[i].shuffle();
        // draw num of member from each group
        print("-"*20);
        for (int j=0; j<num; j++)
        {
          print("group ${i+1}:" + studList[i][j].toString());
        }
      }
    });
}