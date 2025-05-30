SCHEMA = {
  "typeName" : "AWS::EC2::NetworkPerformanceMetricSubscription",
  "description" : "Resource Type definition for AWS::EC2::NetworkPerformanceMetricSubscription",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : { },
  "properties" : {
    "Source" : {
      "description" : "The starting Region or Availability Zone for metric to subscribe to.",
      "type" : "string"
    },
    "Destination" : {
      "description" : "The target Region or Availability Zone for the metric to subscribe to.",
      "type" : "string"
    },
    "Metric" : {
      "description" : "The metric type to subscribe to.",
      "type" : "string"
    },
    "Statistic" : {
      "description" : "The statistic to subscribe to.",
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "required" : [ "Source", "Destination", "Metric", "Statistic" ],
  "createOnlyProperties" : [ "/properties/Source", "/properties/Destination", "/properties/Metric", "/properties/Statistic" ],
  "primaryIdentifier" : [ "/properties/Source", "/properties/Destination", "/properties/Metric", "/properties/Statistic" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ec2:DescribeAwsNetworkPerformanceMetricSubscriptions", "ec2:EnableAwsNetworkPerformanceMetricSubscription" ]
    },
    "read" : {
      "permissions" : [ "ec2:DescribeAwsNetworkPerformanceMetricSubscriptions" ]
    },
    "delete" : {
      "permissions" : [ "ec2:DescribeAwsNetworkPerformanceMetricSubscriptions", "ec2:DisableAwsNetworkPerformanceMetricSubscription" ]
    },
    "list" : {
      "permissions" : [ "ec2:DescribeAwsNetworkPerformanceMetricSubscriptions" ]
    }
  },
  "tagging" : {
    "taggable" : False
  }
}