SCHEMA = {
  "typeName" : "AWS::Logs::ResourcePolicy",
  "description" : "The resource schema for AWSLogs ResourcePolicy",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-logs.git",
  "properties" : {
    "PolicyName" : {
      "description" : "A name for resource policy",
      "type" : "string",
      "pattern" : "^([^:*\\/]+\\/?)*[^:*\\/]+$",
      "minLength" : 1,
      "maxLength" : 255
    },
    "PolicyDocument" : {
      "description" : "The policy document",
      "type" : "string",
      "pattern" : "[\\u0009\\u000A\\u000D\\u0020-\\u00FF]+",
      "minLength" : 1,
      "maxLength" : 5120
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : False
  },
  "primaryIdentifier" : [ "/properties/PolicyName" ],
  "createOnlyProperties" : [ "/properties/PolicyName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "logs:PutResourcePolicy", "logs:DescribeResourcePolicies" ]
    },
    "read" : {
      "permissions" : [ "logs:DescribeResourcePolicies" ]
    },
    "update" : {
      "permissions" : [ "logs:PutResourcePolicy", "logs:DescribeResourcePolicies", "logs:DeleteResourcePolicy" ]
    },
    "delete" : {
      "permissions" : [ "logs:DeleteResourcePolicy" ]
    },
    "list" : {
      "permissions" : [ "logs:DescribeResourcePolicies" ]
    }
  },
  "required" : [ "PolicyName", "PolicyDocument" ]
}