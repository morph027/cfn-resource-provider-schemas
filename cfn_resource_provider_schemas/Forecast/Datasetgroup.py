SCHEMA = {
  "typeName" : "AWS::Forecast::DatasetGroup",
  "description" : "Represents a dataset group that holds a collection of related datasets",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-forecast",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "Arn" : {
      "type" : "string",
      "maxLength" : 256,
      "pattern" : "^[a-zA-Z0-9\\-\\_\\.\\/\\:]+$"
    },
    "MaxResults" : {
      "description" : "The number of items to return in the response.",
      "type" : "integer",
      "minimum" : 1,
      "maximum" : 100
    },
    "NextToken" : {
      "description" : "If the result of the previous request was truncated, the response includes a NextToken. To retrieve the next set of results, use the token in the next request. Tokens expire after 24 hours.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 3000
    }
  },
  "properties" : {
    "DatasetArns" : {
      "description" : "An array of Amazon Resource Names (ARNs) of the datasets that you want to include in the dataset group.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Arn"
      },
      "insertionOrder" : True
    },
    "DatasetGroupName" : {
      "description" : "A name for the dataset group.",
      "type" : "string",
      "pattern" : "^[a-zA-Z][a-zA-Z0-9_]*",
      "minLength" : 1,
      "maxLength" : 63
    },
    "Domain" : {
      "description" : "The domain associated with the dataset group. When you add a dataset to a dataset group, this value and the value specified for the Domain parameter of the CreateDataset operation must match.",
      "type" : "string",
      "enum" : [ "RETAIL", "CUSTOM", "INVENTORY_PLANNING", "EC2_CAPACITY", "WORK_FORCE", "WEB_TRAFFIC", "METRICS" ]
    },
    "Tags" : {
      "description" : "The tags of Application Insights application.",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "minItems" : 0,
      "maxItems" : 200,
      "insertionOrder" : True
    },
    "DatasetGroupArn" : {
      "description" : "The Amazon Resource Name (ARN) of the dataset group to delete.",
      "type" : "string",
      "maxLength" : 256,
      "pattern" : "^[a-zA-Z0-9\\-\\_\\.\\/\\:]+$"
    }
  },
  "additionalProperties" : False,
  "required" : [ "DatasetGroupName", "Domain" ],
  "createOnlyProperties" : [ "/properties/DatasetGroupName" ],
  "readOnlyProperties" : [ "/properties/DatasetGroupArn" ],
  "primaryIdentifier" : [ "/properties/DatasetGroupArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "forecast:CreateDatasetGroup" ]
    },
    "read" : {
      "permissions" : [ "forecast:DescribeDatasetGroup" ]
    },
    "update" : {
      "permissions" : [ "forecast:UpdateDatasetGroup" ]
    },
    "delete" : {
      "permissions" : [ "forecast:DeleteDatasetGroup" ]
    },
    "list" : {
      "permissions" : [ "forecast:ListDatasetGroups" ]
    }
  },
  "taggable" : True
}