SCHEMA = {
  "typeName" : "AWS::MediaTailor::VodSource",
  "description" : "Definition of AWS::MediaTailor::VodSource Resource Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-mediatailor",
  "definitions" : {
    "HttpPackageConfiguration" : {
      "type" : "object",
      "description" : "<p>The HTTP package configuration properties for the requested VOD source.</p>",
      "properties" : {
        "Path" : {
          "type" : "string",
          "description" : "<p>The relative path to the URL for this VOD source. This is combined with <code>SourceLocation::HttpConfiguration::BaseUrl</code> to form a valid URL.</p>"
        },
        "SourceGroup" : {
          "type" : "string",
          "description" : "<p>The name of the source group. This has to match one of the <code>Channel::Outputs::SourceGroup</code>.</p>"
        },
        "Type" : {
          "$ref" : "#/definitions/Type"
        }
      },
      "required" : [ "Path", "SourceGroup", "Type" ],
      "additionalProperties" : False
    },
    "Type" : {
      "type" : "string",
      "enum" : [ "DASH", "HLS" ]
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string",
      "description" : "<p>The ARN of the VOD source.</p>"
    },
    "HttpPackageConfigurations" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/HttpPackageConfiguration"
      },
      "description" : "<p>A list of HTTP package configuration parameters for this VOD source.</p>"
    },
    "SourceLocationName" : {
      "type" : "string"
    },
    "Tags" : {
      "description" : "The tags to assign to the VOD source.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "VodSourceName" : {
      "type" : "string"
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "mediatailor:TagResource", "mediatailor:UntagResource" ]
  },
  "required" : [ "HttpPackageConfigurations", "SourceLocationName", "VodSourceName" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/SourceLocationName", "/properties/VodSourceName" ],
  "primaryIdentifier" : [ "/properties/SourceLocationName", "/properties/VodSourceName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "mediatailor:CreateVodSource", "mediatailor:DescribeVodSource", "mediatailor:TagResource" ]
    },
    "read" : {
      "permissions" : [ "mediatailor:DescribeVodSource" ]
    },
    "update" : {
      "permissions" : [ "mediatailor:DescribeVodSource", "mediatailor:TagResource", "mediatailor:UntagResource", "mediatailor:UpdateVodSource" ]
    },
    "delete" : {
      "permissions" : [ "mediatailor:DeleteVodSource", "mediatailor:DescribeVodSource" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "SourceLocationName" : {
            "$ref" : "resource-schema.json#/properties/SourceLocationName"
          }
        },
        "required" : [ "SourceLocationName" ]
      },
      "permissions" : [ "mediatailor:ListVodSources" ]
    }
  },
  "additionalProperties" : False
}