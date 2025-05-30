SCHEMA = {
  "typeName" : "AWS::Detective::Graph",
  "description" : "Resource schema for AWS::Detective::Graph",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-detective.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. Valid characters are Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @ ",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. Valid characters are Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @ ",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "description" : "The Detective graph ARN"
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "AutoEnableMembers" : {
      "type" : "boolean",
      "default" : False,
      "description" : "Indicates whether to automatically enable new organization accounts as member accounts in the organization behavior graph."
    }
  },
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "detective:UntagResource", "detective:TagResource", "detective:ListTagsForResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "detective:CreateGraph", "detective:ListGraphs", "detective:TagResource", "detective:UpdateOrganizationConfiguration", "organizations:DescribeOrganization" ]
    },
    "update" : {
      "permissions" : [ "detective:ListGraphs", "detective:UntagResource", "detective:TagResource", "detective:ListTagsForResource", "detective:UpdateOrganizationConfiguration", "organizations:DescribeOrganization" ]
    },
    "read" : {
      "permissions" : [ "detective:ListGraphs", "detective:ListTagsForResource", "detective:DescribeOrganizationConfiguration", "organizations:DescribeOrganization" ]
    },
    "delete" : {
      "permissions" : [ "detective:DeleteGraph", "detective:ListGraphs" ]
    },
    "list" : {
      "permissions" : [ "detective:ListGraphs", "detective:ListTagsForResource", "detective:DescribeOrganizationConfiguration", "organizations:DescribeOrganization" ]
    }
  }
}