SCHEMA = {
  "typeName" : "AWS::EC2::InternetGateway",
  "description" : "Allocates an internet gateway for use with a VPC. After creating the Internet gateway, you then attach it to a VPC.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "additionalProperties" : False,
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128,
          "description" : "The tag key."
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "description" : "The tag value."
        }
      },
      "required" : [ "Value", "Key" ],
      "description" : "Specifies a tag. For more information, see [Resource tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html)."
    }
  },
  "properties" : {
    "InternetGatewayId" : {
      "description" : "",
      "type" : "string"
    },
    "Tags" : {
      "description" : "Any tags to assign to the internet gateway.",
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ec2:CreateTags", "ec2:DeleteTags" ]
  },
  "readOnlyProperties" : [ "/properties/InternetGatewayId" ],
  "primaryIdentifier" : [ "/properties/InternetGatewayId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:CreateInternetGateway", "ec2:CreateTags", "ec2:DescribeInternetGateways" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeInternetGateways" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DeleteInternetGateway", "ec2:DescribeInternetGateways" ]
    },
    "update" : {
      "permissions" : [ "ec2:DeleteTags", "ec2:CreateTags", "ec2:DescribeInternetGateways" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeInternetGateways" ]
    }
  }
}