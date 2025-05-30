SCHEMA = {
  "typeName" : "AWS::MediaTailor::LiveSource",
  "description" : "Definition of AWS::MediaTailor::LiveSource Resource Type",
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
      "description" : "<p>The ARN of the live source.</p>"
    },
    "HttpPackageConfigurations" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/HttpPackageConfiguration"
      },
      "description" : "<p>A list of HTTP package configuration parameters for this live source.</p>"
    },
    "LiveSourceName" : {
      "type" : "string"
    },
    "SourceLocationName" : {
      "type" : "string"
    },
    "Tags" : {
      "description" : "The tags to assign to the live source.",
      "type" : "array",
      "uniqueItems" : True,
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
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "mediatailor:TagResource", "mediatailor:UntagResource" ]
  },
  "required" : [ "HttpPackageConfigurations", "LiveSourceName", "SourceLocationName" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/LiveSourceName", "/properties/SourceLocationName" ],
  "primaryIdentifier" : [ "/properties/LiveSourceName", "/properties/SourceLocationName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "mediatailor:CreateLiveSource", "mediatailor:DescribeLiveSource", "mediatailor:TagResource" ]
    },
    "read" : {
      "permissions" : [ "mediatailor:DescribeLiveSource" ]
    },
    "update" : {
      "permissions" : [ "mediatailor:UpdateLiveSource", "mediatailor:DescribeLiveSource", "mediatailor:TagResource", "mediatailor:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "mediatailor:DeleteLiveSource", "mediatailor:DescribeLiveSource" ]
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
      "permissions" : [ "mediatailor:ListLiveSources" ]
    }
  },
  "additionalProperties" : False
}