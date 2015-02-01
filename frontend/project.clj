(defproject frontend "0.1.0-SNAPSHOT"
  :description "FIXME: write this!"
  :url "http://example.com/FIXME"

  :dependencies [[org.clojure/clojure "1.6.0"]
                 [org.clojure/clojurescript "0.0-2322"]
                 [org.clojure/core.async "0.1.338.0-5c5012-alpha"]
                 [org.clojure/google-closure-library "0.0-20140718-946a7d39"]]

  :plugins [[lein-cljsbuild "1.0.4-SNAPSHOT"]]

  :source-paths ["src"]

  :cljsbuild {
    :builds [{:id "frontend"
              :source-paths ["src"]
              :compiler {
                :output-to "frontend.js"
                :output-dir "out"
                :optimizations :none
                :source-map true}}]})
